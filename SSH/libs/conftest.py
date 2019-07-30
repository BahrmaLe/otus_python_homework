import pytest

from SSH.libs.ssh import ShhClient

host = '192.168.56.103'
user = 'akuksenko'
secret = 'toor'
port = 22

# @pytest.fixture
# def ftp_creds(creds):
#     my_ftp = MyFTP(creds[0])
#     my_ftp.connect(creds[1], creds[2])
#     yield my_ftp
#     my_ftp.close()


@pytest.fixture
def ssh_creds():
    ssh = ShhClient(host, user, secret, port)
    yield ssh
    ssh.close()
