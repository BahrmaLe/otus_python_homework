import sys
from ftplib import FTP
from ftplib import all_errors
import logging


class FTPClient:
    """FTP operations"""
    def __init__(self, ftp_host):
        """Inits"""
        self.ftp = FTP(ftp_host)

    def connect(self, user_name, password):
        """Connect"""
        try:
            ftp = self.ftp.login(user=user_name, passwd=password)
            logging.info(ftp)
            return "230" in ftp
        except all_errors as e:
            logging.error(e)
            sys.exit(1)

    def count_files_in_current_directory(self):
        """Count files"""
        files = []
        self.ftp.retrlines("LIST", files.append)
        return len(files)

    def check_file_in_current_directory(self, filename):
        """Check file"""
        directory = []
        self.ftp.retrlines("LIST", directory.append)
        for file in directory:
            if filename in file:
                return True
        return False

    def upload_file(self, filename):
        """Upload"""
        with open(filename, "rb") as f:
            try:
                ftp = self.ftp.storbinary("".join(["STOR ", filename]), f)
                logging.info(ftp)
                return "226" in ftp
            except all_errors as e:
                logging.error(e)
                return False

    def download_file(self, filename, download_filename):
        """Download"""
        with open(download_filename, 'wb') as f:
            try:
                ftp = self.ftp.retrbinary("".join(["RETR ", filename]), f.write)
                logging.info(ftp)
                return "226" in ftp
            except all_errors as e:
                logging.error(e)
                return False

    def create_dir(self, dirname):
        """Create directory"""
        try:
            ftp = self.ftp.mkd(dirname)
            logging.info(ftp)
        except all_errors as e:
            logging.error(e)
            return False

    def delete_dir(self, dirname):
        """Delete directory"""
        try:
            ftp = self.ftp.rmd(dirname)
            logging.info(ftp)
        except all_errors as e:
            logging.error(e)
            return False

    def change_dir(self, dirname):
        """Change directory"""
        try:
            ftp = self.ftp.cwd(dirname)
            logging.info(ftp)
        except all_errors as e:
            logging.error(e)
            return False

    def get_current_dir(self):
        logging.info(self.ftp.pwd())
        return self.ftp.pwd()

    def close(self):
        self.ftp.close()
