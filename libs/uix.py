# -*- coding: utf-8 -*-
import subprocess


MAIN_LOGO = """
$$\       $$\           $$\                      $$\                         
$$ |      \__|          \__|                     $$ |                        
$$ |      $$\  $$$$$$$\ $$\  $$$$$$\  $$$$$$$\ $$$$$$\   $$\   $$\  $$$$$$$\ 
$$ |      $$ |$$  _____|$$ | \____$$\ $$  __$$\\_$$  _|  $$ |  $$ |$$  _____|
$$ |      $$ |\$$$$$$\  $$ | $$$$$$$ |$$ |  $$ | $$ |    $$ |  $$ |\$$$$$$\  
$$ |      $$ | \____$$\ $$ |$$  __$$ |$$ |  $$ | $$ |$$\ $$ |  $$ | \____$$\ 
$$$$$$$$\ $$ |$$$$$$$  |$$ |\$$$$$$$ |$$ |  $$ | \$$$$  |\$$$$$$  |$$$$$$$  |
\________|\__|\_______/ \__| \_______|\__|  \__|  \____/  \______/ \_______/                                                                                                                                                   

$$$$$$$\             $$\                          $$\                        
$$  __$$\            $$ |                         $$ |                       
$$ |  $$ | $$$$$$\ $$$$$$\   $$$$$$$\   $$$$$$\ $$$$$$\                      
$$$$$$$\ |$$  __$$\\_$$  _|  $$  __$$\ $$  __$$\\_$$  _|                     
$$  __$$\ $$ /  $$ | $$ |    $$ |  $$ |$$$$$$$$ | $$ |                       
$$ |  $$ |$$ |  $$ | $$ |$$\ $$ |  $$ |$$   ____| $$ |$$\                    
$$$$$$$  |\$$$$$$  | \$$$$  |$$ |  $$ |\$$$$$$$\  \$$$$  |                   
\_______/  \______/   \____/ \__|  \__| \_______|  \____/   """


MAIN_MENU = """
1. Masscan              (Scan one or diapasons of ip's by specific port/s)
2. Bruteforce           (Bruteforce server/s by ip/s)
3. Send Command         (Send command to remote server. Available cmds: send custom cmd, upload/download file, ddos)

{}

Choose menu item...(1-6)
"""


MSG = """
Result of {}:
Total: {}
Elapsed: {}"""


def show_menu(msg=None):
    subprocess.run(['clear'])

    if msg:
        print(MAIN_LOGO + '\n' + MAIN_MENU.format(msg))
    else:
        print(MAIN_LOGO + '\n' + MAIN_MENU.format(''))


def masscan_start_msg():
    print('Input ip or diapason (ex. 192.168.1.1 or 192.168.1.0/24)')
    ip = input('> ')

    print('Input port/s (ex. 80 or 80,8080,22)')
    port = input('> ')

    subprocess.run(['clear'])

    return ip, port


def bruteforce_start_msg(files_names):
    print('Available list of files for bruteforce.')

    for i in range(len(files_names)):
        print(f'{i}. {files_names[i]}', '\n')

    print('Choose file with hosts from current list. (enter num)')
    choice = input('> ')
    subprocess.run(['clear'])

    return choice


def bruteforce_result_msg(start, stop, hosts_am):
    msg = """Result of bruteforce:
Hacked hosts: {}
Start: {}
Stop: {} 
    """.format(hosts_am, start, stop)

    return msg


def send_command_start_msg():
    msg = """Available commands:
1. Send custom command.
2. Download file from server.
3. Upload file to server.
4. DDos.  (experimental module)     
"""
    print(msg)
    choice = input('> ')
    subprocess.run(['clear'])

    return choice
