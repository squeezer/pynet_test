#!/usr/bin/env python

print('Exercise 16')

inputfilename = 'my_test16_file.txt'

# Exercise16
# a. From your earlier exercise where you parsed the serial number from show_version
# b. Create two functions
# c. Function1 opens the file and returns all of the data in the file as a text string. filename is a function parameter
# d. Function2 parse show_version output and returns the serial number

def Function1(filename = 'my_test16_file.txt'):
    f = open(filename, 'r')
    output = f.readlines()
    f.close()
    return output

def Function2(filedata):
    serialnumber = 'not found'
    for line in filedata:
        if line.startswith('Processor board ID'):
            trash, serialnumber = line.split('ID ')

    return serialnumber

filedata = Function1(inputfilename)
serialnumber = Function2(filedata)

print "Serial number: {}".format(serialnumber)
