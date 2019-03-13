#!/usr/bin/env python

import csv
import sys
import yaml

csv_data=[]
#group_data=[]

# find group to me made
#with open(sys.argv[1]) as csvfile:
#	reader=csv.DictReader(csvfile)
#	for row in reader:
#		if row['hostname'].find("gw") != -1:
#			print ("[gateway]")
#			csv_data.append("[gateway]")
#		if row['hostname'].find("fnkm") != -1:
#			print ("[fnkm]")
#			csv_data.append("[fnkm]")
#		csv_data.append(row)

# find group to me made
#with open(sys.argv[1]) as csvfile:
#print (line['inventory'])


# From the hosts file make the list of inventory groups.
inventory_categories= []
inventory_hosts=[]
with open(sys.argv[2]) as Rngroups:
  group_reader=csv.DictReader(Rngroups)
  for line in group_reader:
    with open('hosts.csv','r') as csvfile:
      reader=csv.DictReader(csvfile)
      for row in reader:
        group_data=row['hostname'].split('-')
        if group_data[-3].strip() == line['fun'].strip():
          inventory_categories.append(line['inventory'])
          inventory_hosts.append(row['hostname'])


print(inventory_categories)
inventory_categories.sort()
print(inventory_categories)
b=set(inventory_categories)
print b
c=list(sorted(set(b)))

print(inventory_hosts)
inventory_hosts.sort()
print(inventory_hosts)
d=set(inventory_hosts)
print d
e=list(sorted(set(d)))
print e
#print c[0]
print filter(lambda x: 'fnk' in x, e)


## Create the inventory file



