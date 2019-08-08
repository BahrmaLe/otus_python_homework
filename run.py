import argparse
import subprocess

a = "C:\\Users\\60064265\\PycharmProjects\\Homework\\API\\tests.py"
b = "/home/akuksenko/otus/otus_python_homework/OpenBreweryDB/tests.py"
c = "C:\\Users\\60064265\\PycharmProjects\\Homework\\CDNJS\\tests.py"
# d = "C:\\Users\\60064265\\GitHub\\otus-qa\\Lesson3\\example1-parametrize\\test_example1_params.py"
names = [a, b, c]

parser = argparse.ArgumentParser()
parser.add_argument('--dogs', action='store_const', const=a, dest="command")
parser.add_argument('--opn', action='store_const', const=b, dest="command")
parser.add_argument('--cdn', action='store_const', const=c, dest="command")
# parser.add_argument('--wrong', action='store_const', const=d, dest="command")
# parser.add_argument("-p", "--path", action="store", dest="command")

args = parser.parse_args()

if args.command not in names:
    raise argparse.ArgumentTypeError("is not allowed directory")

if args.command == a:
    print("Dogs API testing")
elif args.command == b:
    print("openbreweryDB API testing")
elif args.command == c:
    print("CDNJS API testing")
results = (subprocess.check_output(["pytest", "-v", args.command]))
print(results.decode('utf-8'))
# def test_list_of_files():
#     arguments = args()
#     resp = subprocess.check_output(["ls", "-l", arguments.directory]).decode()
#     print(resp)
#     assert "total" in resp
#     logging.info(resp)


# def test_version_package():
#     arguments = args()
#     resp = subprocess.Popen([arguments.package_version, "--version"])
#     resp.communicate()
#     print(resp)
#     assert "version" in resp
#     assert "build" in resp


# def test_proc_info():
#     arguments = args()
#     p1 = subprocess.Popen(["ps", "aux"],
#                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     p2 = subprocess.Popen(["grep", arguments.program_process], stdin=p1.stdout, stdout=subprocess.PIPE)
#     line = p2.stdout.read()
#     print(line.decode())
#     print(line)
#     assert "akuksen+" in line
#
#
# def test_port_activity():
#     arguments = args()
#     p1 = subprocess.Popen(['netstat', '-atnp'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     p2 = subprocess.Popen(["grep", arguments.port_activity], stdin=p1.stdout, stdout=subprocess.PIPE)
#     line = p2.stdout.readline()
#     print(line.decode())
#     assert "unix" in line
#     assert "STREAM" in line