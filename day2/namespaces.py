#!/usr/bin/env python

## Let's talk about namespaces. What does this mean? It means the place
## that variables "live" and the locations you can reference them.

MY_CONST = 'whatever'

def my_func(x, y, z=30): ## These variables are local to this function
    print "Inside my_func"
    x = 40 ## This overrides the Main x here, but not outside of my_func
    print "x: {}".format(x)
    print "y: {}".format(y)
    print "z: {}".format(z)
    print "MY_CONST: {}".format(MY_CONST)

def my_func2():
    # lots and lots of code
    pass

## Use this syntax to designate the "main" part of the script
## Another option is to just define "main()" and then call 
## main() from the bottom.
if __name__ == "__main__":
    x = 10
    y = 20
    z = 31
    my_func(x, y)

    print "Main"
    print "x: {}".format(x)
    print "y: {}".format(y)
    print "z: {}".format(z)

    my_func(4, 5, 6)
