import click
import sys


def say_hello(name):
    click.echo('Hello, {}'.format(name))    # print. python2 compatible


def say_goodbye(name):
    click.echo('Goodbye, {}'.format(name))


@click.option('--bye', is_flag=True, help='say goodbye')
@click.option('--hello', is_flag=True, help='say hello')
@click.option('-v', '--version', is_flag=True, help='show version of this program')
@click.argument('name')
@click.command()
def main(name, version, hello, bye):
    if version:
        print('1.0.0')
        sys.exit()

    if bye:
        say_goodbye(name)
    else:
        say_hello(name)


if __name__ == '__main__':
    main()
