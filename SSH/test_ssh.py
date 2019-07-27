import time
import requests
import paramiko


def test_restart_opencart_services():
    host = '192.168.56.103'
    user = 'akuksenko'
    secret = 'toor'
    port = 22

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user,
                   password=secret, port=port)

    with client.invoke_shell() as ssh:
        ssh.recv(10000).decode("utf-8")
        ssh.send("sudo systemctl restart mysql.service \n")
        ssh.send("".join([secret, "\n"]))
        time.sleep(10)

        ssh.send("sudo systemctl restart apache2.service \n")
        time.sleep(10)

        r = requests.get("/".join(["http:/", host, "opencart"]))
        print(r.status_code)
        assert r.status_code == 200
