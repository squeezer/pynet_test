#!/usr/bin/env python

#Exercise12
#a. Prompt for a network
#b. Always assume /24
#c. Ping the first ten IP addresses of that subnet.
#d. Print out IP addresses where ping was successful

import os

my_network = raw_input("Enter network: ")
octets = my_network.split(".")

for last_octet in range(1, 11):
    octets[-1] = str(last_octet)
    ping_ip =  ".".join(octets) 
    ping_cmd = "ping -c 1 -W 1 {} > /dev/null".format(ping_ip)
    status = os.system(ping_cmd)
    if status == 0:
        print "Ping successful: {}".format(ping_ip)
    else:
        print "Ping unsuccessful: {}".format(ping_ip)

