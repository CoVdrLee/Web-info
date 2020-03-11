#<h1> Webinfo request </h1>
###<h4>Functies:</h4>
* Pull IP from domain
* nameserver lookup
* TXT record lookup
* Simple portscan
    * for standard ports: 20,21,22,23,25,53,67,68,69,80,110,119,123,137,138,139,143,161,162,389,443,445,465,546,547,569,587,990,993,995,1080,1194,3306,3389,3689,5432,5800,5900,6346,8080
    * Samenvatting open porten
##<h4>Code notes</h4>
###<h5>Imported Modules:</h5>
* Socket
```python
ip = socket.gethostbyname(domain)
print("Dit is het IP adress: ",ip)
```
* dns resolvers
```python
answers = dns.resolver.query(domain, 'TXT')
for rdata in answers:
    for txt_string in rdata.strings:
      print ('Dit is het TXT record(s): ', txt_string)
```
* sys
* datetime
```python
final_time = datetime.now()
        print('\n')
        print('You Have Stopped The Scan.\n')
        print('Started At: {}'.format(initial_time))
        print('Finished At: {}'.format(final_time))
```







