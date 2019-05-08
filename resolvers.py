from paramiko import SSHClient, AutoAddPolicy
import logging
from workers import STORAGES, STORAGE_AUTH


def get_files_list(storage_num):
    client = SSHClient()

    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    port = STORAGES[storage_num]
    client.connect('localhost', port, *STORAGE_AUTH)

    stdin, stdout, stderr = client.exec_command('ls /home/fil2es')
    stdout.channel.recv_exit_status()

    output = stdout.read().decode()
    errors = stderr.read().decode()
    if not errors:
        return output
    else:
        logging.error(f'Error while fetching files list: {errors}')
        return False
