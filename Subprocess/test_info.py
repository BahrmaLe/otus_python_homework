import logging
import re
import subprocess

logging.basicConfig(level=logging.INFO)


def test_if():
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
    resp = subprocess.check_output(["tail", "/proc/net/dev"]).decode()
    for line in resp:
        if "enp0s8" in line:
            data = line.split('%s:' % "enp0s8")[1].split()
            rx_bytes, tx_bytes = (data[0], data[8])
            print(rx_bytes, tx_bytes)
# def test_if_stat():
    # resp = subprocess.check_output(["tail", "/proc/net/dev"]).decode()
    # print(resp)
    # pat = re.compile(r'enp0s8: ([1-9]\d*)', re.MULTILINE)
    # print(pat)
    # enp = pat.findall(resp)
    # print(enp)
    # capturedproc = []
    # try:
    #     enp = pat.findall(resp)[0]
    #     print(type(enp))
    #     print(enp)
    #     capturedproc.append(enp)
    #     assert int(enp) > 0
    #     logging.info(enp)
    # except IndexError:
    #     print('No proc match for {}'.format(pat))



def test_service_stat():
    resp = subprocess.check_output(["systemctl", "status", "apache2.service"]).decode("utf-8")
    pat = re.compile(r"Active: (\w*)", re.MULTILINE)
    status = pat.findall(resp)[0]
    logging.info(status)
    assert status == "active"


def test_cur_dir():
    resp = subprocess.check_output(["pwd"]).decode()
    assert "/home/akuksenko/otus/otus_python_homework/Subprocess" in resp
    logging.info(resp)


def test_cernel_version():
    resp = subprocess.check_output(["uname", "-r"]).decode()
    assert "4.15.0-55-generic" in resp
    logging.info(resp)


def test_os_version():
    resp = subprocess.check_output(["cat", "/proc/version"]).decode()
    assert "Ubuntu 7.4.0-1ubuntu1~18.04.1)" in resp
    logging.info(resp)
