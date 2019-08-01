"""
Check package version
List all files in a specified directory
"""
import argparse
import logging
import subprocess
from time import sleep

logging.basicConfig(level=logging.INFO)


def args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', action='store', dest='package', default="bash",
                        help='Get version of the package')
    parser.add_argument('-d', action='store', dest='dir', default=".",
                        help='Get file list in the directory')
    parser.add_argument('--port', action='store', dest='port', default=":21",
                        help='Get file list in the directory')
    parser.add_argument('--program', action='store', dest='program', default="skype",
                        help='Get program info')
    return parser.parse_args()


if __name__ == "__main__":
    # Check version of the package
    arguments = args()
    logging.info("".join(['package =' + arguments.package]))
    logging.info("getting verion info")
    p = subprocess.Popen([arguments.package, "--version"])
    p.communicate()
    sleep(2)

    # Get files in the current directory
    logging.info(arguments.dir)
    logging.info("getting files list")
    resp = subprocess.check_output(["ls", "-l", arguments.dir]).decode()
    print(resp)
    sleep(2)

    logging.info(arguments.port)
    p1 = subprocess.Popen(['netstat', '-atnp'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p2 = subprocess.Popen(["grep", arguments.port], stdin=p1.stdout, stdout=subprocess.PIPE)
    line = p2.stdout.readline()
    print(line.decode())
    sleep(2)

    # Get info about process
    logging.info("".join(["programm ", arguments.program]))
    p1 = subprocess.Popen(["ps", "-o", "pid,ppid,user,args,lstart,etime"],
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p2 = subprocess.Popen(["grep", arguments.program], stdin=p1.stdout, stdout=subprocess.PIPE)
    line = p2.stdout.read()
    print(line.decode())

    print(subprocess.check_output(["ps", "aux"]).decode())






