from SSH.libs.ftp import FTPClient
from SSH.libs.ssh import ShhClient

upload_filename = "test.txt"
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
        ssh.add_ftp_port(2121)
        listen_str = ssh.get_ftp_port()
        assert listen_str == "listen_port=2121\n"

    def test_ftp_installed(self, ssh):
        assert not ssh.check_ftp_installed()


@pytest.mark.usefixture("ftp")
class TestsFTP:
    def test_upload_file(self, ftp):
        assert not ftp.check_file_in_current_directory(filename=upload_filename)
        if ftp.upload_file(filename=upload_filename):
            assert ftp.check_file_in_current_directory(filename=upload_filename)

    def test_create_dir(self, ftp):
        assert not ftp.check_file_in_current_directory(filename=dirname)
        if ftp.create_dir(dirname=dirname):
            assert ftp.check_file_in_current_directory(filename=dirname)

    def test_delete_dir(self, ftp):
        if not ftp.check_file_in_current_directory(filename=dirname):
            ftp.create_dir(dirname)
        if ftp.delete_dir(dirname):
            assert not ftp.check_file_in_current_directory(filename=dirname)

    def test_change_dir(self, ftp):
        if not ftp.check_file_in_current_directory(filename=dirname):
            ftp.create_dir(dirname)
        ftp.change_dir(dirname)
        assert dirname in ftp.get_current_dir()
