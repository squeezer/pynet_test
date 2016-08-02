#!/usr/bin/env python

print('Exercise 4')

my_ip = raw_input('Please enter an IP address: ')
octets = my_ip.split('.')
print "{:>12} {:>12} {:>12} {:>12}".format(octets[0], octets[1], octets[2], octets[3])


