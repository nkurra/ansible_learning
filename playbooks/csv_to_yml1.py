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


# From the hosts file make the list of inventory groups.
with open(sys.argv[2]) as Rngroups:
	group_reader=csv.DictReader(Rngroups)
	for line in group_reader:
		with open('hosts.csv','r') as csvfile:
			reader=csv.DictReader(csvfile)
			for row in reader:
				group_data=row['hostname'].split('-')
				if group_data[-3].strip() == line['fun'].strip():
					print (line['inventory'])
		

#with open(sys.argv[1] + '.yml', 'w') as outfile:
#	outfile.write(yaml.dump({'csv_data':csv_data}))
