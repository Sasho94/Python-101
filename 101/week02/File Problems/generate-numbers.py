
import sys
from random import randint


def main():
    filename = sys.argv[1]
    n = sys.argv[2]

    with open(filename, 'w') as data:
        for i in range(0, int(n)):
            data.write(str(randint(1, 1000)) + " ")

if __name__ == '__main__':
    main()
