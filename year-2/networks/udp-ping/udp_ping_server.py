# from the socket module import all
from socket import *
import random

# create datagram socket
sock = socket(AF_INET, SOCK_DGRAM)

# get hostname
hostname = gethostname()

# get domain name
domainName = getfqdn(hostname)

print('server booting up...')
print("Server Hostname: "+hostname+"\nServer Domain Name: "+domainName)

ipAdd = int(input('Please enter server IP: '))

# bind socket to host and port which is listening on port 6789
serverAddress = (hostname, ipAdd)
sock.bind(serverAddress)

# infinite loop to keep server running and listen for messages from client

while True:

     rand = random.randint(0, 10)

     # receive data, network address and port number for each client request
     data, address = sock.recvfrom(1024)
     data = data.decode() 
     

     print('from client: '+data)


          
     if rand < 4:
          continue

     # extract address and port of client
     clientAddress = address[0]
     clientPort = address[1]
     # print client address and port
     print("\nClient Address: "+clientAddress+"\nClient Port: "+clientPort)
     # echo the received message back to the client

     sock.sendto(data.encode(), (address))