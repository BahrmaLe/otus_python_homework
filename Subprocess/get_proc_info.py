import argparse
import logging
import subprocess


logging.basicConfig(level=logging.INFO)


def args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--program', action='store', dest='program', default="",
                        help='Get program info')
    return parser.parse_args()


if __name__ == "__main__":
    """Get info about process"""
    arguments = args()
    logging.info("".join(["programm ", arguments.program]))
    p1 = subprocess.Popen(["ps", "aux"],
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p2 = subprocess.Popen(["grep", arguments.program], stdin=p1.stdout, stdout=subprocess.PIPE)
    line = p2.stdout.read()
    print(line.decode())

    print(subprocess.check_output(["ps", "aux"]).decode())






