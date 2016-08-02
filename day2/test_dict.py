#!/usr/bin/env python

def my_func(x, y, z=10):
    print "x is: {}".format(x)
    print "y is: {}".format(y)
    print "z is: {}".format(z)
    print "x + y + z is: {}".format(x + y + z)
    return x + y

ret_val = my_func(y=7, x=12)
my_list = [1, 3, 11]

ret_val = my_func(*my_list)

print "x + y = {}".format(ret_val)

