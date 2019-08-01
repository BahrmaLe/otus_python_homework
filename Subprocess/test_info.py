import logging
import re
import subprocess

logging.basicConfig(level=logging.INFO)


def test_if():
    pat_lo = re.compile(b"lo:.*\\n *inet (\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})", re.MULTILINE)
    pat_en = re.compile(b"en.*:.*\\n *inet (\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})", re.MULTILINE)
    pat_wl = re.compile(b"wl.*:.*\\n *inet (\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})", re.MULTILINE)
    resp = subprocess.check_output(["ifconfig"])

    lo_ip = pat_lo.findall(resp)[0].decode()
    wl_ip = pat_wl.findall(resp)[0].decode()

    logging.info(lo_ip)
    logging.info(wl_ip)

    assert lo_ip == "127.0.0.1"
    assert wl_ip == "192.168.56.103"


def test_check_default_route():
    p0 = subprocess.Popen('cmd')
    p1 = subprocess.Popen(['ip', 'r'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p2 = subprocess.Popen(["grep", "default"], stdin=p1.stdout, stdout=subprocess.PIPE)
    line = p2.stdout.readline()
    pat = re.compile(b"default via (\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})")
    ip = re.match(pat, line)
    default_route = ip.group(1).decode()
    logging.info(default_route)
    assert "192.168.56.103" == default_route


def test_processor_info():
    resp = subprocess.check_output("lscpu").decode()
    pat = re.compile(r".*Model name:( *)(.*)", re.MULTILINE)
    model = pat.findall(resp)[0][1]
    assert "i5-8265U" in model
    logging.info(model)


def test_if_stat():
    resp = subprocess.check_output(["tail",  "/proc/net/dev"]).decode()
    pat = re.compile(r"wlp2s0: ([1-9]\d*)", re.MULTILINE)
    wl = pat.findall(resp)[0]
    assert int(wl) > 0
    logging.info(wl)


def test_service_stat():
    resp = subprocess.check_output(["systemctl",  "status", "apache2.service"]).decode()
    pat = re.compile(r"Active: (\w*)", re.MULTILINE)
    status = pat.findall(resp)[0]
    logging.info(status)
    assert status == "active"


def test_cur_dir():
    resp = subprocess.check_output(["pwd"]).decode()
    assert "/home/ksenia/work/otus-qa-course/Lesson23" in resp
    logging.info(resp)


def test_cernel_version():
    resp = subprocess.check_output(["uname", "-r"]).decode()
    assert "4.15.0-1043-oem" in resp
    logging.info(resp)


def test_os_version():
    resp = subprocess.check_output(["cat", "/proc/version"]).decode()
    assert "Ubuntu 7.4.0-1ubuntu1~18.04.1)" in resp
    logging.info(resp)

