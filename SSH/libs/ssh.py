import logging

import paramiko

FTP_DAEMON = "vsftpd.conf"

config = 'listen=NO\n' \
      'listen_ipv6=YES\n' \
      'anonymous_enable=NO\n' \
      'local_enable=YES\n' \
      'write_enable=YES\n' \
      'local_umask=022\n' \
      'dirmessage_enable=YES\n' \
      'use_localtime=YES\n' \
      'xferlog_enable=YES\n' \
      'connect_from_port_20=YES\n' \
      'chroot_local_user=YES\n' \
      'secure_chroot_dir=/var/run/vsftpd/empty\n' \
      'pam_service_name=vsftpd\n' \
      'rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem\n' \
      'rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key\n' \
      'ssl_enable=NO\n' \
      'pasv_enable=Yes\n' \
      'pasv_min_port=10000\n' \
      'pasv_max_port=10100\n' \
      'allow_writeable_chroot=YES\n'
host = '192.168.56.103'
user = 'akuksenko'
secret = 'toor'
port = 22

class ShhClient:
    """Lib"""

    def __init__(self, host, user, secret, port):
        """Init block"""
        self.client = paramiko.SSHClient()
        self.secret = secret
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=host, username=user, password=secret, port=port)

        transport = paramiko.Transport((host, port))
        transport.connect(username=user, password=secret)
        self.sftp = paramiko.SFTPClient.from_transport(transport)

    def close(self):
        self.client.close()

    def execute(self, command):
        """Execution command"""
        stdin, stdout, stderr = self.client.exec_command(command, get_pty=True)
        stdin.write(self.secret + "\n")
        stdin.flush()
        logging.info("{0} - {1}".format(command, stdout.channel.recv_exit_status()))

    def write_file(self, config):
        """Create FTP config """
        f = self.sftp.open("/home/akuksenko/vsftpd.conf", "wb")
        f.write(config)
        f.close()

    def copy_config_file(self):
        """Removing old config and copy new"""
        self.execute("sudo rm /etc/vsftpd.conf")
        self.execute("sudo cp /home/akuksenko/vsftpd.conf /etc/vsftpd.conf")

    def install_ftp(self):
        """Installing FTP DAEMON"""
        self.execute("sudo apt-get install vsftpd")
        self.execute("sudo systemctl start vsftpd")
        self.execute("sudo systemctl enable vsftpd")
        self.write_file(config)
        self.copy_config_file()
        self.restart_ftp()

    def restart_ftp(self):
        """Restating FTP"""
        self.execute("sudo systemctl restart vsftpd ")

    def check_ftp_installed(self) -> object:
        """Checking installation"""
        command = "dpkg -s vsftpd  | grep \"install ok installed\""
        stdin, stdout, stderr = self.client.exec_command(command, get_pty=True)
        data = stdout.read()
        logging.info(data.decode())
        return len(data) == 0

    def create_ftp_user(self, user, password):
        """Create FTP User"""
        self.execute("sudo mkdir /var/ftp_home")
        self.execute("".join(["sudo useradd", user]))
        self.execute("".join(["sudo passwd", user]))
        self.execute(password)
        self.execute(password)
        self.execute("chown {0}:{1} /var/ftp_home".format(user, user))
        self.execute("usermod -d /var/ftp_home/ {0}".format(user))
        
    def check_user(self, user):
        stdin, stdout, stderr = self.client.exec_command("cat /etc/passwd | grep {0}".format(user))
        return len(stdout.read()) > 0

    def delete_ftp_user(self, user):
        """Delete FTP User"""
        self.execute("".join(["sudo userdel", user]))

    def get_ftp_port(self):
        """Show FTP port"""
        stdin, stdout, stderr = self.client.exec_command('cat {0} | grep listen_port '.format(FTP_DAEMON))
        data = stdout.read().decode()
        print(data)
        return data

    def new_listen_port(self, port):
        """Add listen port"""
        self.execute("sudo echo listen_port={0} >> {1}".format(port, FTP_DAEMON))

    def change_ftp_port(self, port):
        """Changing FTP port"""
        self.execute(
            "sudo sed -i 's/.*listen_port=.*/listen_port={0}/' {1}".format(port, FTP_DAEMON))

    def add_ftp_port(self, port):
        """ Add listen port or change """
        listen_port = self.get_ftp_port()
        logging.info(listen_port)
        if not listen_port:
            self.new_listen_port(port)
        else:
            self.change_ftp_port(port)
        self.copy_config_file()
        self.restart_ftp()


