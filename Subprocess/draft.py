"""
Check package version
List all files in a specified directory
"""
import argparse
import logging
import subprocess
from time import sleep

logging.basicConfig(level=logging.INFO)
ssh = 'ssh akuksenko@192.168.56.103'
passwd = 'toor'


parser = argparse.ArgumentParser()

parser.add_argument('--ssh', action='store_const', const=ssh, dest='command', help='Set ssh connection')
parser.add_argument('--passwd', action='store_const', const=passwd, dest='command', help='set a password')

args = parser.parse_args()


# program = "cmd"
# process = subprocess.call(program)

p00 = subprocess.Popen('cmd', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
p0 = subprocess.Popen(['ssh', '-t', '-t', 'akuksenko@192.168.56.103'], shell=True, stdin=p00.stdout, stdout=subprocess.PIPE)
# p1 = subprocess.Popen("toor", shell=True, stdin=p0.stdout,  stdout=subprocess.PIPE)
p2 = subprocess.Popen("ifconfig", shell=True, stdin=p0.stdout, stdout=subprocess.PIPE)
line = p2.stdout.read()
print(line.decode())
sleep(2)
