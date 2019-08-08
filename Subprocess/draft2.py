import re
import argparse
import logging
import subprocess

logging.basicConfig(level=logging.INFO)


def args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', action='store', dest='package_version', default="", help='Get version of the package')
    parser.add_argument('-d', action='store', dest='directory', default="", help='Get file list in the directory')
    parser.add_argument('--port', action='store', dest='port_activity', default="", help='Get port activity')
    parser.add_argument('--program', action='store', dest='program_process', default="", help='Get program info')
    parser.add_argument('--ifconfig', action='store_true', dest='ip_config', default="", help='Get ifconfig info')
    parser.add_argument('--route', action='store_true', dest='route_config', default="", help='Get route')
    parser.add_argument('--cpu', action='store_true', dest='cpu_info', default="", help='Get CPU info')
    parser.add_argument('--net', action='store_true', dest='net_info', default="", help='Get Net stats')
    parser.add_argument('--apache', action='store_true', dest='apache', default="", help='Get Service stats')
    parser.add_argument('--curdir', action='store_true', dest='current_directory', default="", help='Get Current path')
    parser.add_argument('--kernel', action='store_true', dest='kernel_version', default="", help='Get Kernel version')
    parser.add_argument('--os', action='store_true', dest='os_verison', default="", help='Get OS Version')
    return parser.parse_args()


def test_ifconfig():
    pat_local = re.compile(b"lo:.*\\n *inet (\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})", re.MULTILINE)
    pat_enp = re.compile(b"enp0s8.*:.*\\n *inet (\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})", re.MULTILINE)
    resp = subprocess.check_output(["ifconfig"])
    local_ip = pat_local.findall(resp)[0].decode()
    enp0s8_ip = pat_enp.findall(resp)[0].decode()
    logging.info(local_ip)
    logging.info(enp0s8_ip)
    print("Local ip: {}".format(local_ip))
    print("enp0s8: {}".format(enp0s8_ip))
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


def test_apache_stat():
    resp = subprocess.check_output(["systemctl", "status", "apache2.service"]).decode("utf-8")
    if "apache2.service" in resp:
        pat = re.compile(r"Active: (\w*)", re.MULTILINE)
        status = pat.findall(resp)[0]
        # print(resp)
        print(status)
        assert status == "active"
        # return status


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


if __name__ == "__main__":
    arguments = args()

    if arguments.ip_config:
        print(arguments.ip_config)
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_ifconfig"]).decode()
        print(resp)
        raise SystemExit
    elif arguments.route_config:
        print(arguments.route_config)
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_check_default_route"]).decode()
        print(resp)
        raise SystemExit
    elif arguments.cpu_info:
        print(arguments.cpu_info)
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_processor_info"]).decode()
        print(resp)
        raise SystemExit
    elif arguments.net_info:
        print(arguments.net_info)
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_network_bytes"]).decode()
        print(resp)
        raise SystemExit
    elif arguments.apache:
        print(arguments.apache)
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_apache_stat"]).decode()
        print(resp)
        raise SystemExit
    elif arguments.current_directory:
        print(arguments.current_directory)
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_current_dir"]).decode()
        print(resp)
        raise SystemExit
    elif arguments.kernel_version:
        print(arguments.kernel_version)
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_kernel_version"]).decode()
        print(resp)
        raise SystemExit
    elif arguments.os_verison:
        print(arguments.os_verison)
        resp = subprocess.check_output(["pytest", "-s", "-v", "draft2.py::" + "test_os_version"]).decode()
        print(resp)
        raise SystemExit
    elif arguments.package_version:
        arguments = args()
        logging.info("".join(['package =' + arguments.package_version]))
        logging.info("getting verion info")
        p = subprocess.Popen([arguments.package_version, "--version"])
        p.communicate()
        raise SystemExit
    elif arguments.directory:
        logging.info(arguments.directory)
        logging.info("getting files list")
        resp = subprocess.check_output(["ls", "-l", arguments.directory]).decode()
        print(resp)
        raise SystemExit
    elif arguments.port_activity:
        logging.info(arguments.port_activity)
        p1 = subprocess.Popen(['netstat', '-atnp'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p2 = subprocess.Popen(["grep", arguments.port_activity], stdin=p1.stdout, stdout=subprocess.PIPE)
        line = p2.stdout.readline()
        print(line.decode())
        raise SystemExit
    elif arguments.program_process:
        logging.info("".join(["program ", arguments.program_process]))
        p1 = subprocess.Popen(["ps", "-o", "pid,ppid,user,args,lstart,etime"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p2 = subprocess.Popen(["grep", arguments.program_process], stdin=p1.stdout, stdout=subprocess.PIPE)
        line = p2.stdout.read()
        print(line.decode())
        raise SystemExit
