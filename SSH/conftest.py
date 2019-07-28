"""Fixtures"""
import time

import paramiko
import pytest
import requests

host = '192.168.56.103'
user = 'akuksenko'
secret = 'toor'
port = 22


@pytest.fixture()
def restart_mysql():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)

    with client.invoke_shell() as ssh:
        ssh.send("sudo systemctl restart mysql.service \n")
        ssh.send("".join([secret, "\n"]))
        time.sleep(5)

    with client.invoke_shell() as ssh:
        ssh.send("sudo systemctl status mysql.service \n")
        ssh.send("".join([secret, "\n"]))
        time.sleep(5)
        out = ssh.recv(10000).decode("utf-8")
        return out


@pytest.fixture()
def restart_apache():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user,
                   password=secret, port=port)

    with client.invoke_shell() as ssh:
        ssh.send("sudo systemctl restart apache2.service \n")
        ssh.send("".join([secret, "\n"]))
        time.sleep(5)

    with client.invoke_shell() as ssh:
        ssh.send("sudo systemctl status apache2.service \n")
        ssh.send("".join([secret, "\n"]))
        time.sleep(5)
        out = ssh.recv(10000).decode("utf-8")
        return out


@pytest.fixture()
def request_opencart():
    r = requests.get("/".join(["http:/", host, "opencart"]))
    return r
