#!/usr/bin/env python

print('Exercise 9')
#my_test9_file.txt

f = open('my_test9_file.txt','r')

output = f.readlines()

for line in output:
    #print line
    if line.startswith('ROM'):
        preamble, version, release = line.split(',')
        print(version)
    if line.startswith('Processor board ID'):
        trash, serialnumber = line.split('ID ')
        print(serialnumber)
f.close()
