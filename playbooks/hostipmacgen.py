#! /usr/bin/env python
# Used for randomly generating hostnames, ips, and mac addresses
# for testing purposes.
#
__author__ = "Larry Smith Jr."
__email___ = "mrlesmithjr@gmail.com"
__maintainer__ = "Larry Smith Jr."
__status__ = "Development"
# http://everythingshouldbevirtual.com
# @mrlesmithjr
#
import random
import csv
import names

# Define beginning first IP octet
BEG_IP = "10"

# Define DNS suffix to append to hosts
DNS_SUFFIX = "etsbv.internal"

# Define first 3 bytes of MAC address
MAC_1 = 0x02
MAC_2 = 0x16
MAC_3 = 0x3e
NUM_HOSTS = 1000

def randomIP():
    """
    Generates a random IP
    """
    RAN_IP_BITS = ".".join(map(str, (random.randint(0, 255)
                            for _ in range(3))))
    ip =  BEG_IP + "." + RAN_IP_BITS
    return ip
def randomMAC():
    """
    Genrates a random MAC address
    """
    mac = [MAC_1, MAC_2, MAC_3, random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

with open('hosts.csv', 'wb') as csvfile:
    """
    Generates random hostname, inventory_hostname, and writes them along with
    random IP and random MAC to CSV.
    """
    hostsCSV = csv.writer(csvfile, delimiter=",")
    for x in range(NUM_HOSTS):
        hostname = ((str.lower(names.get_last_name())) + '-' +
		                  (str.lower(names.get_first_name()))) + '.' + DNS_SUFFIX
        inventory_name = "server00%s" % x + '.' + DNS_SUFFIX
        ran_ip = randomIP()
        ran_mac = randomMAC()
        item = []
        item.append(hostname)
        item.append(inventory_name)
        item.append(ran_ip)
        item.append(ran_mac)
        if x == 0:
            header = []
            col1 = "inventory_hostname"
            col2 = "inventory_name"
            col3 = "ansible_host"
            col4 = "macaddress"
            header.append(col1)
            header.append(col2)
            header.append(col3)
            header.append(col4)
            hostsCSV.writerow(header)
        hostsCSV.writerow(item)
