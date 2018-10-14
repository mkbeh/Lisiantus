# -*- coding: utf-8 -*-
import subprocess


from bs4 import BeautifulSoup

from libs import utils
from const import MSG


class Masscan(object):
    def __init__(self):
        self.elapsed = None                 # Elapsed time of masscan.
        self.total = None                   # Total found hosts.

    def parse_result_file(self):
        # Read bs object from file.
        with open('masscan_result') as file:
            bs_obj = BeautifulSoup(file, 'lxml-xml')

        self.elapsed = bs_obj.find('finished')['elapsed']
        self.total = bs_obj.find('hosts')['total']
        hosts = bs_obj.findAll('host')

        # Write found data (host:port) in file.
        for host in hosts:
            ip = host.find('address')['addr']
            port = host.find('port')['portid']
            template = f'{ip}\n'

            with open('masscan_hosts_' + port, 'a') as res_file:
                res_file.writelines(template)

    def masscan(self, ip, port):
        command = ['masscan', '-p', f'{port}', f'{ip}', '-oX', 'masscan_result', '--max-rate', '700']
        subprocess.run(command, stdout=subprocess.PIPE, encoding='utf-8')

        self.parse_result_file()
        utils.show_menu(msg=MSG.format('masscan', self.total, self.elapsed))

    def run(self):
        print('Input ip or diapason (ex. 192.168.1.1 or 192.168.1.0/24)')
        ip = input()
        # Need check on valid ip.

        print('Input port/s (ex. 80 or 80,8080,22)')
        port = input()
        # Need to check on valid port.

        subprocess.run(['clear'])
        self.masscan(ip, port)
