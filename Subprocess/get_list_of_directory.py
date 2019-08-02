import argparse
import logging
import subprocess
from time import sleep

logging.basicConfig(level=logging.INFO)


def args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', action='store', dest='dir', default=".",
                        help='Get file list in the directory')
    return parser.parse_args()


if __name__ == "__main__":
    """Get files in the current directory"""
    arguments = args()
    logging.info(arguments.dir)
    logging.info("getting files list")
    resp = subprocess.check_output(["ls", "-l", arguments.dir]).decode()
    print(resp)
    sleep(2)