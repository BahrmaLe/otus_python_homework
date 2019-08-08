import re
import argparse
import logging
import subprocess

logging.basicConfig(level=logging.INFO)


def args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', action='store_true', dest='package_version', default="docker",
                        help='Get version of the package')
    parser.add_argument('-d', action='store_true', dest='directory', default=".",
                        help='Get file list in the directory')
    parser.add_argument('--port', action='store_true', dest='port_activity', default=":21",
                        help='Get port activity')
    parser.add_argument('--program', action='store_true', dest='program_proccess', default="docker",
                        help='Get program info')
    parser.add_argument('--ifconfig', action='store_const', dest='ip_config', const="test_ifconfig",
                        default="test_ifconfig",
                        help='Get ifconfig info')
    parser.add_argument('--route', action='store_const', dest='route_config', const="test_check_default_route",
                        default="test_check_default_route",
                        help='Get route')
    parser.add_argument('--cpu', action='store_const', dest='cpu_info', const="test_processor_info",
                        default="test_processor_info",
                        help='Get CPU info')
    parser.add_argument('--net', action='store_const', dest='net_info', const="test_network_bytes",
                        default="test_network_bytes",
                        help='Get Net stats')
    parser.add_argument('--service', action='store_true', dest='service_status', const="",
                        default="test_service_stat",
                        help='Get Service stats')
    parser.add_argument('--curdir', action='store_const', dest='current_directory', const="test_current_dir",
                        default="test_current_dir",
                        help='Get Current path')
    parser.add_argument('--kernel', action='store_const', dest='kernel_version', const="test_kernel_version",
                        default="test_kernel_version",
                        help='Get Kernel version')
    parser.add_argument('--os', action='store_const', dest='os_verison', const="test_os_version",
                        default="test_os_version",
                        help='Get OS Version')
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
    print(default_route)
    assert "10.0.2.2" == default_route


def test_processor_info():
    resp = subprocess.check_output("lscpu").decode()
    pat = re.compile(r".*Model name:( *)(.*)", re.MULTILINE)
    model = pat.findall(resp)[0][1]
    print(model.decode())
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
    arguments = args()
    resp = subprocess.check_output(["systemctl", "status", arguments.service]).decode("utf-8")
    pat = re.compile(r"Active: (\w*)", re.MULTILINE)
    status = pat.findall(resp)[0]
    logging.info(status)
    print(status)
    assert status == "active"


def test_current_dir():
    resp = subprocess.check_output(["pwd"]).decode()
    print(resp)
    assert "/home/akuksenko/otus/otus_python_homework/Subprocess" in resp
    logging.info(resp)


def test_kernel_version():
    resp = subprocess.check_output(["uname", "-r"]).decode()
    print(resp)
    assert "4.15.0-55-generic" in resp
    logging.info(resp)


def test_os_version():
    resp = subprocess.check_output(["cat", "/proc/version"]).decode()
    print(resp)
    assert "Ubuntu 7.4.0-1ubuntu1~18.04.1)" in resp
    logging.info(resp)


def test_list_of_files():
    arguments = args()
    resp = subprocess.check_output(["ls", "-l", arguments.d]).decode()
    print(resp)
    assert "total" in resp
    logging.info(resp)


def test_version_package():
    arguments = args()
    resp = subprocess.Popen([arguments.p, "--version"])
    resp.communicate()
    print(resp)
    assert "version" in resp
    assert "build" in resp
    logging.info(resp)


def test_proc_info():
    arguments = args()
    p1 = subprocess.Popen(["ps", "aux"],
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p2 = subprocess.Popen(["grep", arguments.program], stdin=p1.stdout, stdout=subprocess.PIPE)
    line = p2.stdout.read()
    print(line.decode())
    print(line)
    assert "akuksen+" in line


def test_port_activity():
    arguments = args()
    p1 = subprocess.Popen(['netstat', '-atnp'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p2 = subprocess.Popen(["grep", arguments.port], stdin=p1.stdout, stdout=subprocess.PIPE)
    line = p2.stdout.readline()
    print(line.decode())
    assert "unix" in line
    assert "STREAM" in line


if __name__ == "__main__":
    arguments = args()

    if arguments.ifconfig:
        print(arguments.ifconfig)
    resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_ifconfig"]).decode()
    print(resp)
    raise SystemExit
    # elif arguments.route:
    #     print(arguments.route_config)
    #     resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_check_default_route"]).decode()
    #     print(resp)
    #     raise SystemExit
    # elif arguments.cpu:
    #     print(arguments.cpu_info)
    #     resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_processor_info"]).decode()
    #     print(resp)
    #     raise SystemExit
    # elif arguments.p:
    #     print(arguments.package_version)
    #     resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_version_package"]).decode()
    #     print(resp)
    #     raise SystemExit
    # elif arguments.d:
    #     print(arguments.directory)
    #     resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_list_of_files"]).decode()
    #     print(resp)
    #     raise SystemExit
    # elif arguments.port:
    #     print(arguments.port_activity)
    #     resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_port_activity"]).decode()
    #     print(resp)
    #     raise SystemExit
    # elif arguments.net:
    #     print(arguments.net_info)
    #     resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_network_bytes"]).decode()
    #     print(resp)
    #     raise SystemExit
    # elif arguments.service:
    #     print(arguments.service_status)
    #     resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_service_stat"]).decode()
    #     print(resp)
    #     raise SystemExit
    # elif arguments.curdir:
    #     print(arguments.current_directory)
    #     resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_current_dir"]).decode()
    #     print(resp)
    #     raise SystemExit
    # elif arguments.kernel:
    #     print(arguments.kernel_version)
    #     resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_kernel_version"]).decode()
    #     print(resp)
    #     raise SystemExit
    # elif arguments.os:
    #     print(arguments.os_verison)
    #     resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_os_version"]).decode()
    #     print(resp)
    #     raise SystemExit
    # elif arguments.program:
    #     print(arguments.program_proccess)
    #     resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_proc_info"]).decode()
    #     print(resp)
    #     raise SystemExit
