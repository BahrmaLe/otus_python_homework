import re
import argparse
import logging
import subprocess

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


def test_service_stat():
    resp = subprocess.check_output(["systemctl", "status", arguments.service]).decode("utf-8")
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


def test_list_of_files():
    resp = subprocess.check_output(["ls", "-l", arguments.command]).decode()
    print(resp)
    assert "total" in resp
    logging.info(resp)


def test_version_package():
    resp = subprocess.Popen([arguments.package, "--version"])
    resp.communicate()
    print(resp)
    assert "version" in resp
    assert "build" in resp
    logging.info(resp)


def test_proc_info():
    p1 = subprocess.Popen(["ps", "aux"],
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p2 = subprocess.Popen(["grep", arguments.program], stdin=p1.stdout, stdout=subprocess.PIPE)
    line = p2.stdout.read()
    print(line.decode())
    print(line)
    assert "akuksen+" in line


def test_port_activity():
    p1 = subprocess.Popen(['netstat', '-atnp'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p2 = subprocess.Popen(["grep", arguments.port], stdin=p1.stdout, stdout=subprocess.PIPE)
    line = p2.stdout.readline()
    print(line.decode())
    assert "unix" in line
    assert "STREAM" in line


def args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', nargs='?', action='store_const', dest='package', const="docker", default="bash",
                        help='Get version of the package')
    parser.add_argument('-d', nargs='?', action='store_const', dest='dir', const=".", default=".",
                        help='Get file list in the directory')
    parser.add_argument('--port', nargs='?', action='store_const', dest='port', const=":21", default=":21",
                        help='Get port activity')
    parser.add_argument('--program', nargs='?', action='store', dest='program', const="docker", default="docker",
                        help='Get program info')
    parser.add_argument('--ifconfig', nargs='?', action='store_const', dest='command', const="test_ifconfig",
                        default=test_ifconfig(),
                        help='Get ifconfig info')
    parser.add_argument('--route', nargs='?', action='store_const', dest='command', const="test_check_default_route",
                        default=test_check_default_route(),
                        help='Get route')
    parser.add_argument('--cpu', nargs='?', action='store_const', dest='command', const="test_processor_info",
                        default=test_processor_info(),
                        help='Get CPU info')
    parser.add_argument('--net', nargs='?', action='store_const', dest='command', const="test_network_bytes",
                        default=test_network_bytes(),
                        help='Get Net stats')
    parser.add_argument('--service', nargs='?', action='store_const', dest='service', const="apache2.service",
                        default=test_service_stat(),
                        help='Get Service stats')
    parser.add_argument('--curdir', nargs='?', action='store_const', dest='command', const="test_current_dir",
                        default=test_current_dir(),
                        help='Get Current path')
    parser.add_argument('--krln', nargs='?', action='store_const', dest='command', const="test_kernel_version",
                        default=test_kernel_version(),
                        help='Get Kernel version')
    parser.add_argument('--os', nargs='?', action='store_const', dest='command', const="test_os_version",
                        default=test_os_version(),
                        help='Get OS Version')
    return parser.parse_args()


if __name__ == "__main__":
    arguments = args()
    if arguments.command == "test_processor_info":
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + arguments.command]).decode()
        print(resp)
        raise SystemExit
    elif arguments.command == "test_check_default_route":
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + arguments.command]).decode()
        print(resp)
        raise SystemExit
    elif arguments.package:
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_version_package"]).decode()
        print(resp)
        raise SystemExit
    elif arguments.dir:
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_list_of_files"]).decode()
        print(resp)
        raise SystemExit
    elif arguments.port:
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_list_of_files"]).decode()
        print(resp)
        raise SystemExit
    elif arguments.command == "test_ifconfig":
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + arguments.command]).decode()
        print(resp)
        raise SystemExit
    elif arguments.command == "test_network_bytes":
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + arguments.command]).decode()
        print(resp)
        raise SystemExit
    elif arguments.service:
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + arguments.service]).decode()
        print(resp)
        raise SystemExit
    elif arguments.command == "test_current_dir":
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + arguments.command]).decode()
        print(resp)
        raise SystemExit
    elif arguments.command == "test_kernel_version":
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + arguments.command]).decode()
        print(resp)
        raise SystemExit
    elif arguments.command == "test_os_version":
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + arguments.command]).decode()
        print(resp)
        raise SystemExit







