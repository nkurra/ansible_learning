#!/usr/bin/env python
import csv,sys,yaml
csv_data=[]

# From the hosts file make the list of inventory groups.
inventory_categories= []
inventory_hosts=[]
inventory_data=dict()
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

inventory_categories.sort()
b=set(inventory_categories)
print b
c=list(sorted(set(b)))
inventory_hosts.sort()
d=set(inventory_hosts)
e=list(sorted(set(d)))

## Create the inventory file
with open(sys.argv[2]) as Rngroups:
  group_reader=csv.DictReader(Rngroups)
  for line in group_reader:
    print (line['inventory'])
    function=line['fun'].strip()
    print "\n" .join(filter(lambda x: function in x, e))
## End of inventory file creation.

# Create the Install.config server list

f = open('Rn_groups.txt', 'r')
newDict = {}
for line in f:
    listedline = line.strip().split(',') # split around the = sign
    if len(listedline) > 1: # we have the = sign in there
        newDict[listedline[0]] = listedline[1]

counter=1
purpose_previous=''
for x in range(len(e)):
  purpose=e[x].split('-')
  with open('hosts.csv', "r") as csvfile2:
    f=csv.DictReader(csvfile2)
    for line in f:
      if line['hostname']==e[x].strip():
        print("SERVER"+"{}" .format(x+1)+"_NAME="+ e[x].strip())
        print("SERVER"+"{}" .format(x+1)+"_IPV4ADDR="+ line['ipaddress'].strip())
        print("SERVER"+"{}" .format(x+1)+"_PURPOSE="+ newDict[purpose[-3]] )
        if counter == 1:
          if purpose_previous.strip() != purpose[-3].strip():
            purpose_previous=purpose[-3]
            counter=1
          else:
            counter=counter+1
        else:
          if purpose_previous==purpose[-3]:
            counter=counter + 1
            purpose_previous=purpose[-3];
          else:
            counter=1
  print("SERVER"+"{}" .format(x)+"_INSTANCE="+str(counter))
  purpose_previous=purpose[-3];
