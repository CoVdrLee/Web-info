#Web info
#website url opvragen van:
#- Nameservers
#- CNAME
#- IP
#- Certificaat
#- Mailserver
#- SPF record
#- txt records

import dns.resolver

domain = 'google.com'
answers = dns.resolver.query(domain,'NS')
for server in answers:
    print(server.target)