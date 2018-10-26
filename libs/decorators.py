# -*- coding: utf-8 -*-
import logging

from libs import utils


def ssh_output(func):
    def wrapper(*args, **kwargs):
        val, log_file_name, cmd = func(*args, **kwargs)     # !!!if no args - set it info into cfg too.
        logging.basicConfig(filename=log_file_name.format(utils.date_today()), level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.info('Output of command {}: {}.'.format(cmd, val))

    return wrapper
