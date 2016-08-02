#!/usr/bin/env python

# Exercise22
# 1. Write a program with three functions (func1, func2, func3)
# 2. Use the if __name__ technique to separate the importable code from the executable code
# 3. Create a main() function and call it.
# 4. Execute the program from the command line. Verify main() function executes
# 5. Go into the Python shell and import the module. Verify main() function does NOT execute.
# 6. In the Python shell look at dir(), __name__, and module.__name__
# 7. Execute pylint on your code.

"""
high level support for doing this and that.
"""

def func1():
    """ high level support for doing this and that. """
    print "func1!"

def func2():
    """ the most important function """
    print "func2!"

def func3():
    """ so important """
    print "func3!"

def main():
    """ the main event """
    print "We are running from the program directly"

if __name__ == "__main__":
    main()
