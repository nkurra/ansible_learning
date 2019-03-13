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
with open(sys.argv[2]) as Rngroups:
#groups_file=open("Rn_groups.txt",'r')
#group_reader=groups_file.readlines()
#print group_reader[3]
#group_reader1=group_reader[2].split(" ")
#print (group_reader1[1])
	group_reader=csv.DictReader(Rngroups)
	#reader=csv.DictReader(csvfile)
	for line in group_reader:
		#print (group_reader1[0])
		#print (line)
		with open('hosts.csv','r') as csvfile:
			reader=csv.DictReader(csvfile)
			for row in reader:
				#group_reader1=line[fun].split(" ")
				#print (row)
				group_data=row['hostname'].split('-')
				#print (group_data[-3])
				#print (line['fun'])
				#if group_data[-3].strip() == group_reader1[0].strip():
				if group_data[-3].strip() == line['fun'].strip():
				#	print (group_reader1[1])
					print (line['inventory'])
		

#with open(sys.argv[1] + '.yml', 'w') as outfile:
#	outfile.write(yaml.dump({'csv_data':csv_data}))
