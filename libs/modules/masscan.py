# -*- coding: utf-8 -*-
import subprocess


from bs4 import BeautifulSoup

from libs import utils
from libs import uix


class Masscan(object):
    def __init__(self):
        self.elapsed = None                 # Elapsed time of masscan.
        self.total = None                   # Total found hosts.
        self.directory = utils.get_path_to_dir('masscan')

    def parse_result_file(self):
        """
        Parse masscan result file and create new file with specific name which contains only ip/s.
        :return:
        """
        date_today = utils.date_today()

        # Read bs object from file.
        with open(self.directory + '/masscan_result') as file:
            bs_obj = BeautifulSoup(file, 'lxml-xml')

        self.elapsed = bs_obj.find('finished')['elapsed']
        self.total = bs_obj.find('hosts')['total']
        hosts = bs_obj.findAll('host')

        # Write found data (host:port) in file.
        for host in hosts:
            ip = host.find('address')['addr']
            port = host.find('port')['portid']
            template = f'{ip}\n'

            with open(self.directory + '/masscan_hosts_' + port + f'_{date_today}', 'a') as res_file:
                res_file.writelines(template)

    def masscan(self, ip, port):
        """
        Method which run mass scanning py ip or file with hosts and port , then parse masscan result file and create
        new with file with specific name.
        :param ip:
        :param port:
        :return:
        """
        command = ['masscan', '-p', f'{port}', f'{ip}', '-oX', self.directory + '/masscan_result', '--max-rate', '700']

        if utils.check_on_file(ip) is True:
            command.insert(3, '-iL')

        subprocess.run(command, stdout=subprocess.PIPE, encoding='utf-8')
        self.parse_result_file()
        uix.show_menu(msg=uix.MSG.format('masscan', self.total, self.elapsed))

    def run(self):
        """
        Method which run masscan module.
        :return:
        """
        ip, port = uix.masscan_start_msg()
        self.masscan(ip, port)
