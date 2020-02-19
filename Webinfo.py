#Web info
#website url opvragen van:
#- Nameservers - Check
#- CNAME -
#- IP
#- Certificaat
#- Mailserver
#- SPF record
#- txt records
counternameserver = 0
nameserverlist = []


import dns.resolver
domain = input ("Wat is het domein naam?: ")

#Opvragen van nameserver
nameservers = dns.resolver.query(domain,'NS')
for server in nameservers:
    counternameserver = counternameserver + 1
    nameserverlist.insert(counternameserver,server.target)


print("de DNS nameservers zijn: ",nameserverlist)
