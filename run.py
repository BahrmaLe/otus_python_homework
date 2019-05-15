import argparse
import subprocess

a = "C:\\Users\\60064265\\PycharmProjects\\Homework\\API\\tests.py"
b = "C:\\Users\\60064265\\PycharmProjects\\Homework\\OpenBreweryDB\\tests.py"
c = "C:\\Users\\60064265\\PycharmProjects\\Homework\\CDNJS\\tests.py"


parser = argparse.ArgumentParser()
# parser.add_argument("-p", "--path", action="store", dest="command")
parser.add_argument('--dogs', action='store_const', const=a, dest="command")
parser.add_argument('--opn', action='store_const', const=b, dest="command")
parser.add_argument('--cdn', action='store_const', const=c, dest="command")

args = parser.parse_args()
# print(args.command)
# This way argument can be manipulated.
if args.command == a:
    print("Dogs API testing")
elif args.command == b:
    print("openbreweryDB API testing")
elif args.command == c:
    print("CDNJS API testing")
results = (subprocess.check_output(["pytest", "-v", args.command]))
print(results.decode('utf-8'))

