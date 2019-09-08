import argparse
import fileinput

from .bridge import init, parse


def main():
    parser = argparse.ArgumentParser(
        description='Bridge for IceNLP')

    parser.add_argument(
        '-s', '--hostname', type=str, default='localhost',
        help='Hostname running IceNLP server')
    parser.add_argument(
        '-p', '--port', type=int, default=1234,
        help='Port running IceNLP server')
    parser.add_argument('filename', nargs='*', help='File to read and parse')

    args = parser.parse_args()

    init(args.hostname, args.port)

    for line in fileinput.input(args.filename):
        print(parse(line))


if __name__ == '__main__':
    main()
