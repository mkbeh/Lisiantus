# -*- coding: utf-8 -*-
import sys
import os
import re


from datetime import datetime


def date_today():
    """
    Func which return today date.
    :return:
    """
    return datetime.today().strftime('%d-%m-%Y-%M-%S').zfill(2)


def get_path_to_dir(dir_name):
    """
    Func which get path to directory by directory name , if directory don't exist - create.
    :param dir_name:
    :return:
    """
    directory = os.path.join(os.path.dirname(sys.argv[0]) + 'results', dir_name)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory


def files_names_filter(seq, filter_word):
    """
    Func witch get sequence of names and filter them by key word.
    :param seq:
    :param filter_word:
    :return:
    """
    for el in seq:
        if filter_word in el:
            yield el


def show_results_files(dir_name, keyword):
    """
    Func which return list of files names from specific directory name.
    :param dir_name:
    :param keyword:
    :return:
    """
    directory = get_path_to_dir(dir_name)
    files = files_names_filter(os.listdir(directory), keyword)

    return list(files)


def get_port_from_file_name(file_name):
    """
    Func which try to search port num in file name.
    :param file_name:
    :return:
    """
    pattern = re.compile('\d\d')

    try:
        return re.search(pattern, file_name).group()
    except AttributeError:
        raise Exception("Port not found in file.")
