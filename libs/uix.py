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
0. Masscan              (Scan one or diapasons of ip's by specific port/s)
1. Bruteforce           (Bruteforce server/s by ip/s)
2. Send Command         (Send command to remote server. Available cmds: send custom cmd, upload/download file, ddos)

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
0. Send custom command to remote servers.
1. Upload payload to remote servers.
2. Download file from remote servers.
3. Upload file to remote servers.
4. Run DDos.  (experimental module)     
"""
    print(msg)
    choice = input('> ')
    subprocess.run(['clear'])

    return choice


def send_command_custom_cmd(dirs_lst):
    print('Available directories with files of hacked hosts:')

    for i in range(len(dirs_lst)):
        print(f'{i}. {dirs_lst[i]}', '\n')

    print('Choose directory:')
    choice = input('> ')
    print('Input your command:')
    cmd = input('> ')
    subprocess.run(['clear'])

    return choice, cmd

