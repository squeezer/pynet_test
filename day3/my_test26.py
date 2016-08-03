#!/usr/bin/env python

# Exercise26
# Connect to the Arista switch
# Configure a vlan with an ID between 100 to 999 (also configure a vlan name)
# Configure this directly from the script and also from a file  

from getpass import getpass
from netmiko import ConnectHandler


def main():
    """Exercises using Netmiko"""
    # 99saturday
    sw1_pass = getpass("Enter switch password: ")

    pynet_sw1 = {
        'device_type': 'arista_eos',
        'ip':   '184.105.247.72',
        'username': 'admin1',
        'password': sw1_pass,
    }

    cfg_commands = [
        'vlan 901',
        'name red',
    ]

    net_connect = ConnectHandler(**pynet_sw1)
    print "Current Prompt: " + net_connect.find_prompt()

    print "\nConfiguring VLAN"
    print "#" * 80
    output = net_connect.send_config_set(cfg_commands)
    print output
    print "#" * 80
    print

    print "\nConfiguring VLAN from file"
    print "#" * 80
    output = net_connect.send_config_from_file("vlan_cfg.txt")
    print output
    print "#" * 80
    print

main()
