#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
import subprocess

from libs import uix

from libs.modules.masscan import Masscan
from libs.modules.bruteforce import Bruteforce
from libs.modules.sendcommand import SendCommand


class Lisiantus(object):
    def __init__(self):
        self.menu_dict = {
            '0': Masscan,               # Masscan
            '1': Bruteforce,            # Bruteforce
            '2': SendCommand,           # Contains: set custom command, upload/download file, ddos.
        }

    def run(self):
        subprocess.run(['clear'])
        uix.show_menu()

        while True:
            choice = input('> ')
            subprocess.run(['clear'])
            self.menu_dict[choice]().run()


if __name__ == '__main__':
    Lisiantus().run()
