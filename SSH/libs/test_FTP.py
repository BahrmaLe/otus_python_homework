import pytest
upload_filename = "C:/Users/60064265/PycharmProjects/Homework/SSH/libs/test.txt"
dirname = "FTP_Directory"


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
        ftp.delete_dir(dirname)
        assert not ftp.check_file_in_current_directory(filename=dirname)

    def test_change_dir(self, ftp):
        if not ftp.check_file_in_current_directory(filename=dirname):
            ftp.create_dir(dirname)
        ftp.change_dir(dirname)
        assert dirname in ftp.get_current_dir()
