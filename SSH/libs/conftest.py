import pytest

from SSH.libs.ftp import FTPClient
from SSH.libs.ssh import ShhClient

host = '192.168.56.103'
user = 'akuksenko'
secret = 'toor'
port = 22


@pytest.fixture
def ftp():
    ftp = FTPClient(ftp_host=host)
    ftp.connect(user_name=user, password=secret)
    yield ftp
    ftp.close()


@pytest.fixture
def ssh():
    ssh = ShhClient(host, user, secret, port)
    yield ssh
    ssh.close()
