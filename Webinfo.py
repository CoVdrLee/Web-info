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
portscankeuze = input("Wilt u ook de meest standaard open poorten checken? (ja/nee)")

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

