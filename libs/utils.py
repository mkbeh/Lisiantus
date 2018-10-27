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
    return datetime.today().strftime('%d-%m-%Y-%H-%M-%S').zfill(2)


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


def values_comparison(val1, val2):
    """
    Func which comparison values and return tuple.
    :param val1:
    :param val2:
    :return:
    """
    return (val1, val2) if val1 < val2 else (val1, val2 + 1)


def split_on_ranges(num, num_ranges, btt_specified=1):
    """
    Func which split number on list of ranges.
    :param num: Number which need split on ranges.
    :param num_ranges: Number of ranges on which need to split number.
    :param btt_specified: Just btt specified param. Need for get correct page num.
    :return:
    """
    last_range = num % num_ranges
    ranges_lst = []

    a = ((num - last_range) / num_ranges * btt_specified).__round__()
    c = a

    for i in range(num_ranges):
        e = 0 if i == 0 else btt_specified
        ranges_lst.append((c - a + e, c))

        if i == num_ranges - 1 and last_range != 0:
            t = values_comparison(c + btt_specified, c + last_range * btt_specified)

            if t[-1] > num:
                ranges_lst.append((t[0],))

            else:
                ranges_lst.append(t)

        else:
            c += a

    return ranges_lst


def get_file_from_dir(directory, hosts_dirs, dir_num, keyword):
    """
    Func which find file by keyword in specific directory.
    :param directory: specific directory
    :param hosts_dirs: list of directories in specific directory
    :param dir_num: required directory number
    :param keyword: keyword which located in file name
    :return:
    """
    files_lst = os.listdir(directory + '/' + hosts_dirs[int(dir_num)])
    required_file = None

    for file in files_lst:
        if keyword in file:
            required_file = file

    path_to_file = directory + '/' + hosts_dirs[int(dir_num)] + '/' + required_file

    return path_to_file


def count_lines(filename, chunk_size=1 << 13):
    """
    Func which count lines in file.
    :param filename:
    :param chunk_size:
    :return:
    """
    with open(filename) as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))


def read_file(file):
    with open(file, 'r') as f:
        for line in f:
            yield line


def create_dict_data(seq):
    for el in list(seq):
        splitted_el = el.split(':')
        yield {'hostname': splitted_el[0], 'username': splitted_el[1], 'password': splitted_el[2]}
