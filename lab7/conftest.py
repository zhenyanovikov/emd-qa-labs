import paramiko
import subprocess
import pytest

server_ip = '10.211.55.7'
password = 'pass'
username = 'parallels'


@pytest.fixture(scope='function')
def server():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_ip, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('iperf3 -s -D')
    data = stderr.read()
    ssh.close()
    return data


@pytest.fixture(scope='function')
def client(server):
    command = 'iperf3 -c ' + server_ip + ' -t 10 -i 1'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    return out, err
