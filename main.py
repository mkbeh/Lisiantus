#!/bin/bash
# -*- coding: utf-8 -*-
import subprocess

import utils

from modules.masscan import Masscan


class Menu(object):
    def __init__(self):
        self.menu_dict = {
            '1': Masscan,               # Masscan
            '2': self.bruteforce,       # Bruteforce
            '3': self.check_alive,      # Check alive servers
            '4': self.upload_data,      # Upload data to client
            '5': self.send_command,     # Send command
            '6': self.ddos              # DDos target (Experimental)
        }

    def masscan(self):
        pass

    def bruteforce(self):
        pass

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
        choice = utils.show_menu()
        self.menu_dict[choice]().run()


if __name__ == '__main__':
    Menu().run()
