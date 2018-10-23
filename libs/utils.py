# -*- coding: utf-8 -*-
import sys
import os


from datetime import datetime


def date_today():
    return datetime.today().strftime('%d-%m-%Y').zfill(2)


def get_path_to_dir(dir_name):
    directory = os.path.join(os.path.dirname(sys.argv[0]) + 'results', dir_name)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory
