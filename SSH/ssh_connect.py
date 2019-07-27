import paramiko
import requests


def test_ssh_connection():
    host = '192.168.56.103'
    user = 'akuksenko'
    secret = 'toor'
    port = 22

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)

    stdin, stdout, stderr = client.exec_command('sudo systemctl stop apache2.service', get_pty=True)
    stdin.write("toor" + "\n")
    stdin.flush()
    stdin, stdout, stderr = client.exec_command('sudo systemctl start apache2.service', get_pty=True)
    stdin.write("toor" + "\n")
    stdin.flush()
    print(stdout.channel.recv_exit_status())
    assert stdout.channel.recv_exit_status() == 0

    stdin, stdout, stderr = client.exec_command('sudo systemctl stop mysql.service', get_pty=True)
    stdin.write("toor" + "\n")
    stdin.flush()

    stdin, stdout, stderr = client.exec_command('sudo systemctl start mysql.service', get_pty=True)
    stdin.write("toor" + "\n")
    stdin.flush()
    print(stdout.channel.recv_exit_status())
    assert stdout.channel.recv_exit_status() == 0

    r = requests.get("/".join(["http:/", host, "opencart"]))
    assert r.status_code == 200
    print(r.status_code)
    client.close()

