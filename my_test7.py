#!/usr/bin/env python

print('Exercise 7')

my_ip = raw_input('Please enter an IP address: ')
octets = my_ip.split('.')
octets[-1] = 0

octets_converted = []

for octet in octets:
    octets_converted.append(bin(int(octet)))

print octets_converted

print "{:>12} {:>12} {:>12} {:>12}".format(octets[0], octets[1], octets[2], octets[3])


