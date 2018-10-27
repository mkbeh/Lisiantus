# -*- coding: utf-8 -*-
import logging

from libs import utils


def ssh_output(func):
    def wrapper(*args, **kwargs):
        val, log_file_name, cmd, host, log = func(*args, **kwargs)

        if log == 'y':
            logging.basicConfig(filename=log_file_name.format(utils.date_today()), level=logging.INFO,
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logging.info(f'Host: {host}. Output of command {cmd}:\n{val}.')

    return wrapper
