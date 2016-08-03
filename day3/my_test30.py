#!/usr/bin/env python

# Exercise 30
# Use eapi to retrieve 'show ip route' from your arista switch.
# From the returned data structure retrieve the prefixes, the output interfaces, and the next hops
# (if available).
# Print these routes and associated information to standard out.

from pprint import pprint
import pyeapi
from getpass import getpass

def main():
    """
    Use eapi to retrieve 'show ip route' from your arista switch.
    From the returned data structure retrieve the prefixes, the output interfaces, and the next hops
    (if available).
    Print these routes and associated information to standard out.
    """

    #sw1_pass = getpass("Enter switch PW: ")
    # 99saturday

    #pynet_switch1 = {
    #    'device_type': 'arista_eos',
    #    'ip':   '184.105.247.72',
    #    'username': 'admin1',
    #    'password': sw1_pass,
    #}

    pynet_sw1 = pyeapi.connect_to("pynet-sw3")
    output = pynet_sw1.enable("show ip route")

    # Strip off unneeded information
    output = output[0]
    output = output['result']['vrfs']['default']

    # Get the routes
    routes = output['routes']
    print "\n{:>15} {:>15} {:>15}".format("prefix", "interface", "next_hop")
    filler = "-" * 15
    print "{:>15} {:>15} {:>15}".format(filler, filler, filler)
    for prefix, attr in routes.items():
        intf_nexthop = attr['vias'][0]
        interface = intf_nexthop.get('interface', 'N/A')
        next_hop = intf_nexthop.get('nexthopAddr', 'N/A')
        print "{:>15} {:>15} {:>15}".format(prefix, interface, next_hop)
    print

if __name__ == "__main__":
    main()