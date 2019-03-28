import argparse


def hello(name):
    print('Hello, {}'.format(name))


def bye(name):
    print('Good bye, {}'.format(name))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='write name you want to say hello')
    args = parser.parse_args()
    name = args.name
    hello(name)


if __name__ == "__main__":
    main()
