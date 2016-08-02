#!/usr/bin/env python

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

def read_file(filename = 'my_test19_file.txt'):
    file_contents = open(filename)
    data = file_contents.readlines()
    file_contents.close()
    return data

def get_vendor(file_contents):
    vendor = 'not found'
    for line in file_contents:
        if line.startswith('Copyright'):
            trash, vendor = line.split('by ')
    return vendor.strip()

def get_model_number(file_contents):
    model_number = 'not found'
    for line in file_contents:
        if 'processor' in line:
            model_number, trash = line.split(' processor ')
    return model_number

def get_os_version(file_contents):
    os_version = 'not found'
    for line in file_contents:
        if 'RELEASE SOFTWARE' in line:
            trash, version = line.split(' Version ')
            os_version, trash = version.split(', ')
    return os_version

def get_serial_number(file_contents):
    serial_number = 'not found'
    for line in file_contents:
        if line.startswith('Processor board ID'):
            trash, serial_number = line.split('ID ')

    return serial_number.strip()

def get_uptime(file_contents):
    uptime = 'not found'
    for line in file_contents:
        if 'uptime is' in line:
            trash, uptime = line.split('uptime is ')
    return uptime.strip()

data = read_file('my_test19_file.txt')
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

