import argparse
import logging
import subprocess
from time import sleep

logging.basicConfig(level=logging.INFO)


def args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', action='store', dest='package', default="bash",
                        help='Get version of the package')
    return parser.parse_args()


if __name__ == "__main__":
    # Check version of the package
    arguments = args()
    logging.info("".join(['package =' + arguments.package]))
    logging.info("getting verion info")
    p = subprocess.Popen([arguments.package, "--version"])
    p.communicate()
    sleep(2)
