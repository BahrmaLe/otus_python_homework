import json
import os
import re
import sys
from collections import Counter
from operator import itemgetter


class AccessLogger:
    """Class for parsing logs"""
    report = {}

    def __init__(self, filename):
        """log filename and reads file"""
        self.log_name = filename
        try:
            with open(self.log_name) as f:
                self.log_file = f.read()
        except IOError:
            print(" ".join(["Can not find file", self.log_name]))
            sys.exit(1)

    def _set_report_value_(self, key, value):
        """Adding value to a dictionary"""
        self.report[key] = value

    def requests(self):
        """All requests"""
        regexp = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        ips_list = re.findall(regexp, self.log_file)
        self._set_report_value_("Count all requests", len(ips_list))

    def request_by_type(self):
        """All requests by type"""
        regexp = r"GET|POST|PUT|DELETE"
        access_requests = re.findall(regexp, self.log_file)
        self._set_report_value_("Requests by type", dict(Counter(access_requests)))

    def last_ten_ips(self):
        """Last ten ip"""
        regexp = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        ips_list = re.findall(regexp, self.log_file)
        dict_ip_sorted_by_desc = map(lambda x: x[0], sorted(Counter(ips_list).items(), key=itemgetter(1),
                                                            reverse=True)[:10])
        self._set_report_value_("Last ten ip", list(dict_ip_sorted_by_desc))

    def last_ten_longest_requests(self):
        """Longest requests"""
        regexp = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*)(POST|GET)(.*?)( 2\d\d )(\d*)(.*?)(http:.*?")'
        longest_logs = re.findall(regexp, self.log_file)
        longest_logs_info = list(map(lambda x: (x[2], x[7], x[0], x[5]), longest_logs))
        sorted_list = sorted(Counter(longest_logs_info).items(), key=itemgetter(1), reverse=True)[:10]
        self._set_report_value_("Last ten longest requests", list(map(lambda x: x[0], sorted_list)))

    def last_ten_client_errors(self):
        """Client errors"""
        regexp = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*)(POST|GET)(.*?)( 4\d\d )(.*?)(http:.*?")'
        client_error_logs = re.findall(regexp, self.log_file)
        client_error_logs_info = list(map(lambda x: (x[0], x[2], x[4], x[6]), client_error_logs))
        sorted_list = sorted(Counter(client_error_logs_info).items(), key=itemgetter(1), reverse=True)[:10]
        self._set_report_value_("Last ten client errors", list(map(lambda x: x[0], sorted_list)))

    def last_ten_server_errors(self):
        """Server errors"""
        regexp = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*)(POST|GET)(.*?)( 5\d\d )(.*?)(http:.*?")'
        client_error_logs = re.findall(regexp, self.log_file)
        client_error_logs_info = list(map(lambda x: (x[0], x[2], x[4], x[6]), client_error_logs))
        sorted_list = sorted(Counter(client_error_logs_info).items(), key=itemgetter(1), reverse=True)[:10]
        self._set_report_value_("Last ten server error", list(map(lambda x: x[0], sorted_list)))

    def save_to_json(self):
        """Saving report to json"""
        base_name = os.path.basename(self.log_name).split('.')[0]
        full_path = "\\".join([os.path.dirname(self.log_name), base_name])
        full_path = "".join([full_path, '.json'])
        with open(full_path, 'w') as json_file:
            json.dump(self.report, json_file)

    def analyze_all(self):
        """Analyzing all logs"""
        self.requests()
        self.request_by_type()
        self.last_ten_ips()
        self.last_ten_longest_requests()
        self.last_ten_client_errors()
        self.last_ten_server_errors()
        self.save_to_json()
