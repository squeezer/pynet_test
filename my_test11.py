#!/usr/bin/env python

#Exercise11
#1.  Create a list containing the values 1-49
#2.  Loop over this list, printing each value
#3.  Use continue to skip over 13 (not print it)
#4. Break when you hit 39 (stop printing after this and exit the loop)

my_list = range (1,50)
for item in my_list:
    if item == 13:
        continue
    if item == 39:
        print item
        break
    print item
