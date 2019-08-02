import logging
import re
import subprocess
import argparse
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
    parser.add_argument('--program', action='store', dest='program', default="",
                        help='Get program info')
    return parser.parse_args()


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


def test_network_bytes():
    resp = subprocess.check_output(["tail", "/proc/net/dev"]).decode("utf-8")
    print(resp)
    if "enp0s8" in resp:
        data = resp.split('%s:' % "enp0s8")[1].split()
        rx_bytes, tx_bytes = (data[0], data[8])
        print("Received bytes: {}".format(rx_bytes))
        print("Transmit bytes: {}".format(tx_bytes))
        assert int(rx_bytes) > 0
        assert int(tx_bytes) > 0


def test_apache_service_stat():
    resp = subprocess.check_output(["systemctl", "status", "apache2.service"]).decode("utf-8")
    pat = re.compile(r"Active: (\w*)", re.MULTILINE)
    status = pat.findall(resp)[0]
    logging.info(status)
    assert status == "active"


def test_current_dir():
    resp = subprocess.check_output(["pwd"]).decode()
    assert "/home/akuksenko/otus/otus_python_homework/Subprocess" in resp
    logging.info(resp)


def test_kernel_version():
    resp = subprocess.check_output(["uname", "-r"]).decode()
    assert "4.15.0-55-generic" in resp
    logging.info(resp)


def test_os_version():
    resp = subprocess.check_output(["cat", "/proc/version"]).decode()
    assert "Ubuntu 7.4.0-1ubuntu1~18.04.1)" in resp
    logging.info(resp)


if __name__ == "__main__":
    # Check version of the package
    arguments = args()
    if args() == "package":
        print("Getting package version")
        logging.info("".join(['package =' + arguments.package]))
        logging.info("getting verion info")
        p = subprocess.Popen([arguments.package, "--version"])
        p.communicate()
        sleep(2)

    if args() == "dir":
        print("Getting files in the current directory")
        # Get files in the current directory
        logging.info(arguments.dir)
        logging.info("getting files list")
        resp = subprocess.check_output(["ls", "-l", arguments.dir]).decode()
        print(resp)
        sleep(2)

    if args() == "port":
        print("Getting port activity")
        logging.info(arguments.port)
        """getting port state"""
        p1 = subprocess.Popen(['netstat', '-atnp'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p2 = subprocess.Popen(["grep", arguments.port], stdin=p1.stdout, stdout=subprocess.PIPE)
        line = p2.stdout.readline()
        print(line.decode())
        sleep(2)

    if args() == "program":
        print("Getting info about process")
        # Get info about process
        logging.info("".join(["programm ", arguments.program]))
        p1 = subprocess.Popen(["ps", "aux"],
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p2 = subprocess.Popen(["grep", arguments.program], stdin=p1.stdout, stdout=subprocess.PIPE)
        line = p2.stdout.read()
        print(line.decode())


#     print(subprocess.check_output(["ps", "aux"]).decode())
#
#     if args() == "package":
#         print("Getting package version")
#     if args()  == "dir":
#         print("openbreweryDB API testing")
# elif args.command == c:
#     print("CDNJS API testing")
# results = (subprocess.check_output(["pytest", "-v", args.command]))
# print(results.decode('utf-8'))
