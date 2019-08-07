"""
Check package version
List all files in a specified directory
"""
import re
import argparse
import logging
import subprocess
from time import sleep

logging.basicConfig(level=logging.INFO)


def test_ifconfig():
    pat_local = re.compile(b"lo:.*\\n *inet (\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})", re.MULTILINE)
    pat_enp = re.compile(b"enp0s8.*:.*\\n *inet (\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})", re.MULTILINE)
    resp = subprocess.check_output(["ifconfig"])

    local_ip = pat_local.findall(resp)[0].decode()
    enp0s8_ip = pat_enp.findall(resp)[0].decode()

    logging.info(local_ip)
    logging.info(enp0s8_ip)

    assert local_ip == "127.0.0.1"
    assert enp0s8_ip == "192.168.56.103"


def test_check_default_route():
    p1 = subprocess.Popen(['ip', 'r'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p2 = subprocess.Popen(["grep", "default"], stdin=p1.stdout, stdout=subprocess.PIPE)
    line = p2.stdout.readline()
    pat = re.compile(b"default via (\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})")
    ip = re.match(pat, line)
    default_route = ip.group(1).decode()
    logging.info(default_route)
    assert "10.0.2.2" == default_route


def test_processor_info():
    resp = subprocess.check_output("lscpu").decode()
    pat = re.compile(r".*Model name:( *)(.*)", re.MULTILINE)
    model = pat.findall(resp)[0][1]
    assert "Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz" in model
    logging.info(model)


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
    parser.add_argument('--ifconfig', action='store_const', dest='command', const="test_ifconfig",
                        default=test_ifconfig(),
                        help='Get ifconfig info')
    parser.add_argument('--route', action='store_const', dest='command', const="test_check_default_route",
                        default=test_check_default_route(),
                        help='Get route')
    parser.add_argument('--cpu', action='store_const', dest='command', const="test_processor_info",
                        default=test_processor_info(),
                        help='Get CPU info')
    return parser.parse_args()


if __name__ == "__main__":
    arguments = args()
    resp = subprocess.check_output(["pytest", "-s", "-v" "draft2.py::", arguments.command]).decode()
    print(resp)
    sleep(2)

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






