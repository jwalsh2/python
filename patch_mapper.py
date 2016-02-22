#! /usr/bin/python
# all files assumed in the same path
# takes output as txt or csv from the CMDB or other list of servers
# compares to list of RHEL6 and RHEL7 servers that need a given patch and creates output
# of servers in the CMDB needing a patch

name = raw_input('Enter the name of the Input File (csv) from CMDB: ')
if len(name) <1 : name = 'cisearch_servers_IN_2016_0221.csv'

fh = open(name)
cmdb = list()
row = list()

for line in fh:
    delimiter = ','
    line = line.split(delimiter)
    svr = line[0].split(' ')
   # print svr[0] removes trailing HEX from vCD
    row = (svr[0], line[13], line[2])
    cmdb.append(row)   
# print cmdb # Debug line

name2 = raw_input('Enter name of the Satellite Export File for Red Hat 6: ')
if len(name2) <1 : name2 = 'RHLE6-glibc.csv'

fh = open(name2)
rh6 = list()
rh6svr = list()


for line in fh:
    delimiter = ','
    line = line.split(delimiter)
    # go clean up the FQDN, drop after the .
    rh6svr = line[0].split('.')
    rh6.append(rh6svr[0])

name3 = raw_input('Enter name of the Satellite Export File for Red Hat 7: ')
if len(name3) <1 : name3 = 'RHLE7-glibc.csv'

fh = open(name3)
rh7 = list()
rh7svr = list()

for line in fh:
    delimiter = ','
    line = line.split(delimiter)  
    # go clean up the FQDN, drop after the .
    rh7svr = line[0].split('.')    
    rh7.append(rh7svr[0])

# rh6 is a list that has the scrubbed names of RHEL 6 servers
# rh7 is a list that has the scrubbed names of RHEL 7 servers
    
print'========================================================================='
print 'Servers in the CMDB: ', len(cmdb)
print 'Red Hat 6 servers needing patch: ',len(rh6)
print 'Red Hat 7 servers needing patch: ',len(rh7)


rh6patch = list()
rh7patch = list()
svr2 = list()

fout6 = open('rh6patch.txt', 'w')
fout7 = open('rh7patch.txt', 'w')

for server in cmdb:
#    svr2 = server[1].split('.')
    if server[0] in rh6:
        rh6patch.append(server[0])
        fout6.write(server[0]+'\n')
        #if svr2[0] not in rh6:
            #rh6patch.append(svr2[0])
            #fout6.write(svr2[0]+'\n')        
        #if server[1] not in rh6:
            #rh6patch.append(server[1])
            #fout6.write(server[1]+'\n')
       
            
    if server[0] in rh7:
        rh7patch.append(server[0])
        fout7.write(server[0]+'\n')
        #if server[2] in rh7:
            #rh7patch.append(server[2])
            #fout7.write(server[2]+'\n')            

print ' '
print '... ... Calculating and Creating Output Files ... ... '
print ' '
print 'Red Hat 6 Servers in CMDB needing patch: ',len(rh6patch), '- written to rh6patch.txt'
print 'Red Hat 7 Servers in CMDB needing patch: ',len(rh7patch), '- written to rh7patch.txt'

# cleaning up

fout6.close()
fout7.close()
