# -*- coding: utf-8 -*-
import json
import logging

from libs import utils


def ssh_send_cmd_out(func):
    """
    SSH send command output decorator.
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        lst = list(func(*args, **kwargs))

        for el in lst:
            val, log_file_name, cmd, host, log = el

            if log == 'y':
                data = {
                    'date': utils.date_today(),
                    'host': host,
                    'cmd': cmd,
                    'output': val,
                }

                logging.basicConfig(filename=log_file_name, format='', level=logging.INFO)
                logging.info(json.dumps(data))

    return wrapper
