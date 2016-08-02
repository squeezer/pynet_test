#!/usr/bin/env python


## Let's write some functions to log in, enable, and get all
## text on one page on a switch.

def login(telnet_conn):
    # log in
    pass

def enable(telnet_conn):
    # enable mode on switch
    pass

def disabling_paging(telnet_conn):
    # all text on one page, no paging
    pass

## This is annoying! Why? Because you have all these functions that 
## need the same piece of data. In this case, we should be using
## classes and objects!
## What are classes/objects? Shared data and functions!

## How do we do this?

class NetDevice(object): # In python 2, use "object".
    def __init__(self, ip_addr, username,password):
        ## What is self? It's a reference to the object. An instance
        ## of the NetDevice class in this case.
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

    def test_method(self):
        print "Device IP is: {}".format(self.ip_addr)
        print "Username is: {}".format(self.username)

rtr1 = NetDevice('10.22.1.1', 'admin', 'passw')
rtr2 = NetDevice('172.16.25.25', 'bob', 'password')

rtr1.test_method()
rtr2.test_method()

print rtr1.ip_addr


