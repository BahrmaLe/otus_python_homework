from socket import *
import re


class Requests:
    """Class with requests"""
    header_dict = {}
    body = []
    status_code_text = ""
    status_code = ""
    data = ""

    def __init__(self, request):
        """Init block"""
        server = request.config.getoption("--server")
        port = request.config.getoption("--port")
        method = request.config.getoption("--method")
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((server, port))
        method = "".join([method, "HTTP/1.1\r\nHost:", server, "\r\n\r\n"])
        self.sock.send(method.encode())

        while True:
            d = self.sock.recv(1024).decode()
            self.data = "".join([self.data, d])
            if not d:
                break
        self.sock.close()

    def text(self):
        """Get HTML body as text"""
        rx_sequence = re.compile(r"(?i)<!doctype html>(.*\n)*", re.MULTILINE)
        for match in rx_sequence.finditer(self.data):
            self.body = match.group(0)
        return self.body

    def headers(self):
        """Get headers"""
        str_list = re.split("\\n", self.data)
        for s in str_list:
            s = s.rstrip()
            headers_re = "(.*): (.*)"
            res = re.match(headers_re, s)
            if res:
                self.header_dict[res.group(1)] = res.group(2)
        return self.header_dict

    def get_status_code(self):
        """Get status code"""
        header_status_re = r"HTTP\/1.\d (\d{3}) (.*)"
        res = re.match(header_status_re, self.data)
        self.status_code = res.group(1).rstrip()
        self.status_code_text = res.group(2).rstrip()
        return int(self.status_code)




