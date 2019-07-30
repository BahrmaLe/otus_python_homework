from SSH.libs.ftp import FTPClient
from SSH.libs.ssh import ShhClient

upload_filename = "test.txt"
dirname = "FTP_Directory"
host = '192.168.56.103'
user = 'akuksenko'
secret = 'toor'
port = 22


def test_install_vsftpd():
    ssh = ShhClient(host, user, secret, port)
    if ssh.check_ftp_installed():
        ssh.install_ftp()
        assert not ssh.check_ftp_installed()
    ssh.close()


def test_create_user():
    ssh = ShhClient(host, user, secret, port)
    if "cat: ftp_user: No such file or directory" in ssh.check_user("ftp_user"):
        ssh.create_ftp_user("ftp_user", "1111")
    assert "/home/ftp_user/:bin/sh" in ssh.check_user("ftp_user")
    ssh.close()


def test_delete_user():
    ssh = ShhClient(host, user, secret, port)
    if ssh.check_user("ftp_user"):
        ssh.delete_ftp_user("ftp_user")
    assert not ssh.check_user("ftp_user")
    ssh.close()


def test_change_port():
    ssh = ShhClient(host, user, secret, port)
    ssh.add_ftp_port(2121)
    listen_str = ssh.get_ftp_port()
    assert listen_str == "listen_port=2121\n"
    ssh.close()


def test_ftp_installed():
    ssh = ShhClient(host, user, secret, port)
    assert not ssh.check_ftp_installed()


def test_upload_file():
    """Uploading file test"""
    ftp = FTPClient(host)
    ftp.connect(user, secret)
    assert not ftp.check_file_in_current_directory(filename=upload_filename)
    if ftp.upload_file(filename=upload_filename):
        assert ftp.check_file_in_current_directory(filename=upload_filename)
    ftp.close()


def test_create_dir():
    ftp = FTPClient(host)
    ftp.connect(user, secret)
    assert not ftp.check_file_in_current_directory(filename=dirname)
    if ftp.create_dir(dirname=dirname):
        assert ftp.check_file_in_current_directory(filename=dirname)


def test_delete_dir():
    ftp = FTPClient(host)
    ftp.connect(user, secret)
    if not ftp.check_file_in_current_directory(filename=dirname):
        ftp.create_dir(dirname)
    if ftp.delete_dir(dirname):
        assert not ftp.check_file_in_current_directory(filename=dirname)


def test_change_dir():
    ftp = FTPClient(host)
    ftp.connect(user, secret)
    if not ftp.check_file_in_current_directory(filename=dirname):
        ftp.create_dir(dirname)
    ftp.change_dir(dirname)
    assert dirname in ftp.get_current_dir()
