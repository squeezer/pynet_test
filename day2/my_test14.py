#!/usr/bin/env python

print('Exercise 14 - Dictionaries')

network_device = {} # deliberately not using {'key': value} here 
network_device['ip_address'] = '8.8.8.8'
network_device['username'] = 'mq'
network_device['password'] = 'passw0rd1'
network_device['vendor'] = 'Palo Alto Networks'
network_device['model'] = 'Widget 5000'


for key, value in network_device.iteritems():
    print key, value

network_device['secret'] = 'Very secret'
network_device['password'] = 'new passw0rd1'

print(r'Checking device type...')
device_type = network_device.get('device_type', 'cisco_ios')
print device_type
