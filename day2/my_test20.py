#!/usr/bin/env python


# Exercise 20 / 21
# re-write exercise 19, but using regular expressions.

# Exercise19
# Parse show version and obtain
# Vendor
# Model Number
# OS version
# Serial number
# uptime
# Read this from a file
# For each of the above parsing use a function
# Save this information to a dictionary
# Print out the dictionary keys and values using pprint

import re

def read_file(filename = 'my_test20_file.txt'):
    file_contents = open(filename)
    data = file_contents.readlines()
    file_contents.close()
    return data

def get_vendor(file_contents):
    pattern = 'Copyrigh.* by (.*)'
    vendor = 'not found'
    for line in file_contents:
        match = re.search(pattern, line)
        if match:
            vendor = match.group(1)
    return vendor

def get_model_number(file_contents):
    pattern = '(.*?) processor.*'
    model_number = 'not found'
    for line in file_contents:
        match = re.search(pattern, line)
        if match:
            model_number = match.group(1)
    return model_number

def get_os_version(file_contents):
    pattern = 'ROM: Sy.* Version (.*?),'
    os_version = 'not found'
    for line in file_contents:
        match = re.search(pattern, line)
        if match:
            os_version = match.group(1)
    return os_version

def get_serial_number(file_contents):
    pattern = 'Processor board ID (.*)'
    serial_number = 'not found'
    for line in file_contents:
        match = re.search(pattern, line)
        if match:
             serial_number = match.group(1)
    return serial_number.strip()

def get_uptime(file_contents):
    pattern = '.* uptime is (.*)'
    uptime = 'not found'
    for line in file_contents:
        match = re.search(pattern, line)
        if match:
            uptime = match.group(1)
    return uptime.strip()

data = read_file('my_test20_file.txt')
#print "Data: {}".format(data)
 
vendor = get_vendor(data)
model_number = get_model_number(data)
os_version = get_os_version(data)
serial_number = get_serial_number(data)
uptime = get_uptime(data)

print "Vendor: {}".format(vendor)
print "Model number: {}".format(model_number)
print "OS Version: {}".format(os_version)
print "Serial number: {}".format(serial_number)
print "Uptime: {}".format(uptime)



#>>> pattern
#'ROM: Sy.* Version (.*?),'
#>>> for line in lines:
#...     re.search(pattern, line)
#... 
#<_sre.SRE_Match object at 0x7feba613c210>
#>>> for line in lines:
#...     if re.search(pattern, line):
#...         print('We have a match. Line = %s' % line)
#... 
#We have a match. Line = ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

#>>> for line in lines:
#...     match = re.search(pattern, line)
#...     if match:
#...         print match.group(1)
