import subprocess
import re
import paramiko
from scp import SCPClient

getDate = subprocess.getstatusoutput("date")

# Send the available address to a txt file

with open ('/root/python/availableAddress/allIpAddress.txt' , 'r') as allIpAddress:
    for ip in allIpAddress:
        com = subprocess.getstatusoutput('ping -c 2' + ' ' + str(ip))
        if "Unreachable" in com[1]:
            ipAddRex = re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", com[1]).group()
            print ("This address is available: " + ipAddRex)
            with open ('/root/python/availableAddress/availableAddress.txt' , 'a') as availableAddress:
                availableAddress.write("This address is available: " + ipAddRex + "\n")
        else:
            print (com[1])

with open ('/root/python/availableAddress/availableAddress.txt' , 'a') as availableAddress:
    availableAddress.write("\n" + "################ Avilable address to this day: " + str(getDate[1]) + " ################" + "\n" + "\n")
            
# Send the txt file to TrueNAS (or another Linux Machine)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='1.1.1.1', 
            port = '22',
            username='username',
            password='password')

scp = SCPClient(ssh.get_transport())
scp.put('/root/python/availableAddress/availableAddress.txt', '/mnt/Home-Storage/bigdata/dvir-data')
scp.close()
