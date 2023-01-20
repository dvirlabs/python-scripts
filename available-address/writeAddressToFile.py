import ipaddress

with open ('/root/python/availableAddress/allIpAddress.txt' , 'w') as allIpAddress:

    for ip in ipaddress.IPv4Network('192.168.1.0/24'):
        allIpAddress.write(str(ip))
        allIpAddress.write('\n')