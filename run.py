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

args = parser.parse_args()-

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

