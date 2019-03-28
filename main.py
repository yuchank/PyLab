import jinja2


def cuckoo_create():

    rtemplate = jinja2.Environment().from_string(open('init-pre.jinja2', "rb").read())
    data = rtemplate.render()


def cuckoo_init():
    cuckoo_create()


def cuckoo_main():
    return


def main():
    cuckoo_init()
    cuckoo_main()


if __name__ == '__main__':
    main()
