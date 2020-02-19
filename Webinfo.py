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

# TXT record
answers = dns.resolver.query('google.com', 'TXT')
print(' query qname:', answers.qname, ' num ans.', len(answers))
for rdata in answers:
    for txt_string in rdata.strings:
      print (' TXT:', txt_string)


print("de DNS nameservers zijn: ",nameserverlist)
