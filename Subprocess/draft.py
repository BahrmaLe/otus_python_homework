import subprocess

sshProcess = subprocess.Popen(['ssh', "192.168.56.103"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, bufsize=0)
sshProcess.stdin.write("ls .\n")
sshProcess.stdin.write("echo END\n")
sshProcess.stdin.write("uptime\n")
sshProcess.stdin.write("logout\n")
sshProcess.stdin.close()


for line in sshProcess.stdout:
    if line == "END\n":
        break
    print(line,end="")

for line in sshProcess.stdout:
    if line == "END\n":
        break
    print(line,end="")