# -*- coding: utf-8 -*-
import sys
import os
import re
import linecache

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

    # Will run if num ranges * 2 >= num.
    if num <= (num_ranges*2):
        lst = [i for i in range(num + 1)]

        return lst[0], lst[-1]

    # Will run if num >= num of ranges.
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
    """
    Read file by line.
    :param file:
    :return:
    """
    with open(file, 'r') as f:
        for line in f:
            yield line


def read_file_from_specific_line(file, range_, lock):
    """
    Read file from specific line.
    :param file:
    :param range_:
    :param lock:
    :return:
    """
    begin = range_[0] if range_[0] != 0 else 1

    with lock:
        for line_num in range(begin, range_[1] + 1):
            yield linecache.getline(file, line_num)


def create_dict_data(seq):
    """
    Create dict from specific data.
    :param seq:
    :return:
    """
    for el in list(seq):
        splitted_el = el.split(':')
        yield {'hostname': splitted_el[0], 'username': splitted_el[1], 'password': splitted_el[2]}


def check_on_not_eq_vals(val1, val2):
    """
    Func which check values on non equivalent and return tuple of vals.
    :param val1:
    :param val2:
    :return:
    """
    return (val1, val2) if val1 != val2 else (val1,)


def check_difference_on_lt(val1, val2):
    """
    Func which calculate difference of values and check it on __lt__ num 20.
    Additional func for func split_on_ranges_by_step.
    :param val1:
    :param val2:
    :return:
    """
    difference = val2 - val1

    if difference < 20:     # < 20 are nums on which func split on rages return incorrect ranges.
        return val1, val2


def split_on_ranges_by_step(begin, end, num_ranges):
    """
    Func which beginning split on ranges num from param begin to param end by step.
    :param begin:
    :param end:
    :param num_ranges:
    :return:
    """
    last_val = (end - begin) % num_ranges
    end_ = end - last_val
    step = round((end - begin) / num_ranges) if last_val == 0 else round((end_ - begin) / num_ranges)
    lst = []
    result = check_difference_on_lt(begin, end)

    if result:
        lst.append(result)
        return lst

    for count, i in enumerate(range(begin, end_, step)):
        if count == 0:
            lst.append((i, i + step))

        else:
            lst.append((i + 1, i + step))

            if count == num_ranges - 1 and last_val != 0:
                lst.append(check_on_not_eq_vals(i + step + 1, i + step + last_val))

    return lst


def check_on_file(val):
    """
    Func which check val on ip or exist file.
    :param val:
    :return:
    """
    pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')

    try:
        re.match(pattern, val).group()
        return
    except AttributeError:
        bool_ = os.path.isfile(val)

        if bool_ is False:
            raise Exception(f'{val} does\'nt exist.')

        return bool_
