# -*- coding: utf-8 -*-
import json

from libs import utils


def ssh_send_cmd_out(func):
    """
    SSH send command output decorator.
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        val, log_file_name, cmd, host, log = func(*args, **kwargs)

        if log == 'y':
            data = {
                'date': utils.date_today(),
                'host': host,
                'cmd': cmd,
                'output': val,
            }

            with open(log_file_name, 'a') as f:
                f.write(json.dumps(data))

    return wrapper
