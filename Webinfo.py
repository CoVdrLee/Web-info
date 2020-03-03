#Web info
#- Nameservers - Check
#- CNAME -
#- Certificaat
#- Mailserver

counternameserver = 0
nameserverlist = []
port = 80
import socket
import dns.resolver
domain = input ("Wat is het domein naam?: ")
portscan = input("Wilt u ook de meest standaard open poorten checken? (ja/nee)")

if (portscan == "ja" or portscan == "Ja" or portscan == "JA" or portscan == "J" or portscan == "j"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((domain, port))
    if result == 0:
        print ("port",port ,"is open")
    else:
        print("port",port ,"is not open")
    sock.close()


ip = socket.gethostbyname(domain)
print("Dit is het IP adress: ",ip)

#Opvragen van nameserver
nameservers = dns.resolver.query(domain,'NS')
for server in nameservers:
    counternameserver = counternameserver + 1
    nameserverlist.insert(counternameserver,server.target)
print("Dit zijn de DNS nameservers: ", nameserverlist)

# TXT record
answers = dns.resolver.query(domain, 'TXT')
for rdata in answers:
    for txt_string in rdata.strings:
      print ('Dit is het TXT record(s): ', txt_string)

