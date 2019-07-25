"""Parse logs"""
import argparse
import os

from AccessLog.parser_access_log import AccessLogger


def create_parser():
    """Command line options"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', default="C:/Users/60064265/PycharmProjects/Homework/AccessLog/logs/",
                        help="Logs Directory")

    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    apache_log = ""
    if os.path.exists(namespace.dir):
        if os.path.isfile(namespace.dir):
            apache_log = AccessLogger(namespace.dir)
        elif os.path.isdir(namespace.dir):
            files = os.listdir(namespace.dir)
            for file in files:
                if os.path.splitext(os.path.basename(file))[1] == '.log':
                    apache_log = AccessLogger("".join([namespace.dir, file]))
        if apache_log:
            apache_log.analyze_all()
    else:
        print("not found")

