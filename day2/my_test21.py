#!/usr/bin/env python

# Exercise 21
# 1. re-write exercise 20, but use a class to contain all the functions (methods)
# 2. save the serial_number, model, vendor, uptime, os_version to the object
# 3. Print out these values from the object

import re

class NetworkDevice(object):
    def __init__(self, data):
        print "Initializing a new NetworkDevice object!"
        self.data = data

    def show_information(self):
        self.vendor = self.get_vendor()
        self.model_number = self.get_model_number()
        self.os_version = self.get_os_version()
        self.serial_number = self.get_serial_number()
        self.uptime = self.get_uptime()

        print "Vendor: {}".format(self.vendor)
        print "Model number: {}".format(self.model_number)
        print "OS Version: {}".format(self.os_version)
        print "Serial number: {}".format(self.serial_number)
        print "Uptime: {}".format(self.uptime)

    def get_vendor(self):
        pattern = 'Copyrigh.* by (.*)'
        vendor = 'not found'
        for line in self.data:
            match = re.search(pattern, line)
            if match:
                vendor = match.group(1)
        return vendor

    def get_model_number(self):
        pattern = '(.*?) processor.*'
        model_number = 'not found'
        for line in self.data:
            match = re.search(pattern, line)
            if match:
                model_number = match.group(1)
        return model_number

    def get_os_version(self):
        pattern = 'ROM: Sy.* Version (.*?),'
        os_version = 'not found'
        for line in self.data:
            match = re.search(pattern, line)
            if match:
                os_version = match.group(1)
        print('We are in the %s object' % self)
        return os_version

    def get_serial_number(self):
        pattern = 'Processor board ID (.*)'
        serial_number = 'not found'
        for line in self.data:
            match = re.search(pattern, line)
            if match:
                serial_number = match.group(1)
        return serial_number.strip()

    def get_uptime(self):
        pattern = '.* uptime is (.*)'
        uptime = 'not found'
        for line in self.data:
            match = re.search(pattern, line)
            if match:
                uptime = match.group(1)
        return uptime.strip()

def read_file(filename = 'my_test21_file.txt'):
    file_contents = open(filename)
    data = file_contents.readlines()
    file_contents.close()
    return data

data = read_file('my_test21_file.txt')
data2 = read_file('my_test21_file-2.txt')

router1 = NetworkDevice(data)
router2 = NetworkDevice(data2)

router1.show_information()
print('-----------')
router2.show_information()

