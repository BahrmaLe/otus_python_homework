import argparse
import logging
import subprocess
from time import sleep

logging.basicConfig(level=logging.INFO)


def args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--port', action='store', dest='port', default="",
                        help='Get file list in the directory')

    return parser.parse_args()


if __name__ == "__main__":
    """Get port activity"""
    arguments = args()
    logging.info(arguments.port)
    p1 = subprocess.Popen(['netstat', '-atnp'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p2 = subprocess.Popen(["grep", arguments.port], stdin=p1.stdout, stdout=subprocess.PIPE)
    line = p2.stdout.readline()
    print(line.decode())
    sleep(2)
