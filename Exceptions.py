#trap error
mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

key = input('please input a key: ')

try:
    print('testing the error')
    print('the value for {0} is {1}'.format(key, mydict[key]))
    print('everything is ok')

except KeyError:
    print('trapped error')
    print('the key' + key + 'does not exist')

print('program continues....')

#trap two errors in a tuple
import sys

try:
    arg = sys.argv[1]
    num = int(arg)

except(IndexError, ValueError):
    exit('please enter an integer')

#raise error
def make_delim_file(list_to_join, delim):

    try:
        formatted_line = delim.join(list_to_join)
    except TypeError:
        raise TypeError('make_delim_error(): arg 1 must be a list or tuple')
    return formatted_line

fline = make_delim_file(100, ',')

#
try:
    print(5/0)
except ZeroDivisionError as e:
    #print(e.message)
    print(e.args)

#custom exceptions
class MyError(Exception):
    def __init__(self, *args):
        print('calling init')
        if args:
            self.message = args[0]
        else:
            self.message = ''

    def __str__(self):
        print('calling str')
        if self.message:
            return 'MyError exception with message: {0}'.format(self.message)
        else:
            return'MyError exception'

#raise MyError()

raise MyError('we have a problem')