# Author Anand
# dir(sys)
# help(sys.exit)
# help(len)

import sys


def Hello(name):
    if name == 'Anand' or name == 'Anand':
        print('Alert Anand mode ')
    else:
        print('Normal mode')
    name = name + '!!!!'
    print('Hello', name.lower())
    print(name.find('a'))
    print(name[0])

    print(name[1:3])
    print(name[:-4])
    print(name[-3:])
    print(len(sys.argv))


# Define main() functiom that prints a little greetings
def main():
    print('Hello')
    print(sys.argv)
    a = "Welcome to Python"
    print(len(a))

    Hello(sys.argv[1])

# This is a standard boilerplate that calls the main() function

if __name__ == '__main__':
    main()

