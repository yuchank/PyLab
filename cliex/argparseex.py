import argparse
import sys


def hello(name):
    print('Hello, {}'.format(name))


def bye(name):
    print('Good bye, {}'.format(name))


def main():
    parser = argparse.ArgumentParser()
    # nargs='?': if no arg, use default value
    parser.add_argument('name', nargs='?', default=False, help='write name you want to say hello')
    parser.add_argument('-v', '--version', action='store_true', help='show version of this program')
    # exclusive options
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--hello', action='store_true', help='say hello')
    group.add_argument('--bye', action='store_true', help='say good bye')
    args = parser.parse_args()
    name = args.name

    if args.version:
        print('1.0.0')
        sys.exit()

    if not name:
        parser.print_help()
        sys.exit()

    if args.bye:
        bye(name)
    else:
        hello(name)


if __name__ == "__main__":
    main()
