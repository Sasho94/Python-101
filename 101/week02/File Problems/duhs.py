import sys
import os

RESULT = 0


def calculate_size(root):

    files = os.listdir(root)
    rs = 0
    for f in files:
        if os.path.isfile(root + '/' + f):
            res = os.stat(root + '/' + f).st_size
            print root + '/' + f
            print res

        else:
            calculate_size(root + '/' + f)


def main():

    result = calculate_size("/home/alexander/101/")
    print result


if __name__ == '__main__':
    main()
