import argparse
import subprocess
import logging
from Subprocess import test_info
from Subprocess.test_info import test_ifconfig, test_check_default_route, test_processor_info

# a = "C:\\Users\\60064265\\PycharmProjects\\Homework\\API\\tests.py"
# b = "C:\\Users\\60064265\\PycharmProjects\\Homework\\OpenBreweryDB\\tests.py"
# c = "C:\\Users\\60064265\\PycharmProjects\\Homework\\CDNJS\\tests.py"
# d = "C:\\Users\\60064265\\GitHub\\otus-qa\\Lesson3\\example1-parametrize\\test_example1_params.py"
# names = [a, b, c]

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser()
# parser.add_argument('-d', action='store_const', dest='dir', const=".", default=".",
#                         help='Get file list in the directory')
# parser.add_argument('--port', action='store_const', dest='port', const="80", default="80",
#                         help='Get file list in the directory')
# parser.add_argument('--program', action='store_const', dest='program', const="docker", default="docker",
#                         help='Get program info')
# parser.add_argument('-p', action='store_const', dest='package', const="docker", default="docker",
#                         help='Get version of the package')
parser.add_argument('--ifconfig', action='store_const', dest='package', const=test_ifconfig(), default=test_ifconfig(),
                        help='Get ifconfig info')
parser.add_argument('--route', action='store_const', dest='package', const=test_check_default_route(), default=test_check_default_route(),
                        help='Get route')
parser.add_argument('--cpu', action='store_const', dest='package', const=test_processor_info(), default=test_processor_info(),
                        help='Get CPU info')


# parser.add_argument('--dogs', action='store_const', const=a, dest="command")
# parser.add_argument('--opn', action='store_const', const=b, dest="command")
# parser.add_argument('--cdn', action='store_const', const=c, dest="command")
# parser.add_argument('--wrong', action='store_const', const=d, dest="command")
# parser.add_argument("-p", "--path", action="store", dest="command")

args = parser.parse_args()

# if args.command not in names:
#     raise argparse.ArgumentTypeError("is not allowed directory")
if __name__ == "__main__":
    if args.command == test_ifconfig():
        print("Checking ifconfig info")
    elif args.command == test_check_default_route():
        print("Checking default route")
    elif args.command == test_processor_info():
        print("Checking CPU")
    results = (subprocess.check_output(["pytest", "-s", "-v", args.command]))
    print(results.decode('utf-8'))

