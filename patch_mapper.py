#! /usr/bin/python
# all files assumed in the same path
# takes output as txt or csv from the CMDB or other list of servers
# compares to list of RHEL6 and RHEL7 servers that need a given patch and creates output
# of servers in the CMDB needing a patch

name = raw_input('Enter the name of the Input File (csv) from CMDB: ')
if len(name) <1 : name = 'CMDB_RHEL_InSVC_2016_0217.csv'

fh = open(name)
cmdb = list()
for line in fh:
    delimiter = ','
    line = line.split(delimiter)
    # print 'Server name: ',line[0]
    cmdb.append(line[0])
# print cmdb

name2 = raw_input('Enter name of the Satellite Export File for Red Hat 6: ')
if len(name2) <1 : name2 = 'RHLE6-glibc.csv'

fh = open(name2)
rh6 = list()

for line in fh:
    delimiter = ','
    line = line.split(delimiter)  
    rh6.append(line[0])
    
name3 = raw_input('Enter name of the Satellite Export File for Red Hat 7: ')
if len(name3) <1 : name3 = 'RHLE7-glibc.csv'

fh = open(name3)
rh7 = list()

for line in fh:
    delimiter = ','
    line = line.split(delimiter)  
    rh7.append(line[0])
    
print'========================================================================='
print 'Servers in the CMDB: ', len(cmdb)
print 'Red Hat 6 servers needing patch: ',len(rh6)
print 'Red Hat 7 servers needing patch: ',len(rh7)
rh6patch = list()
rh7patch = list()

fout6 = open('rh6patch.txt', 'w')
fout7 = open('rh7patch.txt', 'w')

for server in cmdb:
    if server in rh6:
        rh6patch.append(server)
        fout6.write(server+'\n')
    if server in rh7:
        rh7patch.append(server)
        fout7.write(server+'\n')

print ' '
print '... ... Calculating and Creating Output Files ... ... '
print ' '
print 'Red Hat 6 Servers in CMDB needing patch: ',len(rh6patch), '- written to rh6patch.txt'
print 'Red Hat 7 Servers in CMDB needing patch: ',len(rh7patch), '- written to rh7patch.txt'

# cleaning up

fout6.close()
fout7.close()
