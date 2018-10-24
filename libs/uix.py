# -*- coding: utf-8 -*-
import subprocess

from const import MAIN_MENU, MAIN_LOGO


def show_menu(msg=None):
    subprocess.run(['clear'])

    if msg:
        print(MAIN_LOGO + '\n' + MAIN_MENU.format(msg))
    else:
        print(MAIN_LOGO + '\n' + MAIN_MENU.format(''))


def masscan_start_msg():
    print('Input ip or diapason (ex. 192.168.1.1 or 192.168.1.0/24)')
    ip = input('> ')

    print('Input port/s (ex. 80 or 80,8080,22)')
    port = input('> ')

    subprocess.run(['clear'])

    return ip, port


def bruteforce_start_msg(files_names):
    print('Available list of files for bruteforce.')

    for i in range(len(files_names)):
        print(f'{i}. {files_names[i]}', '\n')

    print('Choose file with hosts from current list. (enter num)')
    choice = input('> ')
    subprocess.run(['clear'])

    return choice


def bruteforce_result_msg(start, stop, hosts_am):
    msg = """
Result of bruteforce:
Hacked hosts: {}
Start: {}
Stop: {} 
    """.format(hosts_am, start, stop)

    return msg
