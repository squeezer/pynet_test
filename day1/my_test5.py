#!/usr/bin/env python

f = open('my_test5.txt')

output = f.readlines()

outfile = open('my_test5_output.txt', 'w')

for line in output:
    print line
    outfile.write(line)
    outfile.write('\n')

f.close()
outfile.close()

outfile = open('my_test5_output.txt', 'a')
outfile.write('One last thing to add... \n')
outfile.close()
