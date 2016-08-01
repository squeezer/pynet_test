#!/usr/bin/env python

f = open('my_test10_file.txt')

output = f.readlines()

for line in output:
    if line.startswith(' *'):
        prettyline = line[5:-2]
        #print prettyline
        network = prettyline[:17].strip()
        nexthop = prettyline[17:32].strip()
        path = prettyline[58:].strip()
        print(r'Network: %s, Next hop: %s, Path: %s' % (network,nexthop,path))
f.close()

