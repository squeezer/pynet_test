#!/usr/bin/env python

# Exercise17
# a. Construct a function that has three parameters x, y, z
# b. z has a default value of 20
# c. Return x + y + z
# d. Call this function using all three positional arguments
# e. Call this function using named arguments x, y (let z be the default)
# f. Call this function with one positional argument and two named arguments.
# g. Call this function using three strings.
# h. Call this function using three lists.

print('Exercise 17\n___________')

def function_parameters(x, y, z = 20, *args, **kwargs):
    return x+y+z

print function_parameters(1, 2, 3)
print function_parameters(y=1, x=2)
print function_parameters(3, z=2, y=1)
print function_parameters('bob', ' mary', ' sue')

x = ['first',' second',' third']
y = ['fourth',' fifth',' sixth']
z = ['seventh',' eighth',' ninth']

print function_parameters(*x)
print function_parameters(*y)
print function_parameters(*z)
