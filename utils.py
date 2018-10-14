# -*- coding: utf-8 -*-
import subprocess

from const import MAIN_MENU, MAIN_LOGO


def show_menu(msg=None):
    subprocess.run(['clear'])

    if msg:
        print(MAIN_LOGO + '\n' + MAIN_MENU.format(msg))
    else:
        print(MAIN_LOGO + '\n' + MAIN_MENU.format(''))

    choice = input()
    subprocess.run(['clear'])

    return choice
