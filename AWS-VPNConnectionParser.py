#!/usr/bin/python


name = raw_input('Enter the name of the VPN Configuration File: ')
vpcname = raw_input('What is the VPC name eg nit-et-ia:')
vpnloc = raw_input('Which ASR is this for eg abbt or lev:')

output = vpcname + "-" + vpnloc + ".txt"

search = open(name)
write = open(output, 'w')

for line in search:
    if '! Your VPN Connection ID' in line:
        #print(line)
        write.write(line)
    if '! Your Virtual Private Gateway ID' in line:
        #print(line)
        write.write(line)
    if '! Your Customer Gateway ID' in line:
        #print(line)
        write.write(line)
    if '! #' in line:
        #print(line)
        write.write(line)
    if '! -' in line:
        #print(line)
        write.write(line)
    if '! IPSec' in line:
        #print(line)
        write.write(line)
    if '!' in line:
        pass
    else:
        #print(line)
        write.write(line)

search.close()
write.close()
