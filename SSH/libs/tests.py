from SSH.libs.ftp import FTPClient
from SSH.libs.ssh import ShhClient

upload_filename = "C:/Users/60064265/PycharmProjects/Homework/SSH/libs/test.txt"
dirname = "FTP_Directory"


import pytest


@pytest.mark.usefixture("ssh")
class TestsSSH:
    def test_install_vsftpd(self, ssh):
        if ssh.check_ftp_installed():
            ssh.install_ftp()
            assert not ssh.check_ftp_installed()

    def test_create_user(self, ssh):
        if not ssh.check_user_ftp("ftp_user"):
            ssh.create_ftp_user("ftp_user", "1111")
        assert ssh.check_user_ftp("ftp_user")

    def test_delete_user(self, ssh):
        if ssh.if_user_exist("ftp_user"):
            ssh.delete_ftp_user("ftp_user")
        assert not ssh.if_user_exist("ftp_user")

    def test_change_port(self, ssh):
        ssh.add_ftp_port(21)
        listen_str = ssh.get_ftp_port()
        assert listen_str == "listen_port=21\n"

    def test_ftp_installed(self, ssh):
        assert not ssh.check_ftp_installed()
