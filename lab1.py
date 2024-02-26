import requests
import datetime
import time


url= input("Give url: ")   

response=requests.get(url)
headers=response.headers

print("Τα headers είναι: \n\n")
for key,value in headers.items():
    print(key,":",value,"\n")

server=headers.get('Server')
if server:
    print("\nΤο λογισμικό που χρησιμοποιεί ο εξυπηρετητής (ο web server) για να απαντήσει στο αίτημα είναι: ",server)
else:
    print("Server not found")

if(len(response.cookies)==0):print("Η σελίδα δεν χρησιμοποιεί cookies")
else:
    print("Η σελίδα  χρησιμοποιεί cookies\n")
    cookie_header= headers['Set-Cookie']
    print(cookie_header,"\n\n")


for cookie in response.cookies:

    print("Cookie name: ",cookie.name)
    try:
        print('Expiration Date(local time): ',datetime.datetime.fromtimestamp(cookie.expires).strftime('%c'))
        remaining=   cookie.expires- int(time.time())
        print("Time left to expire: ", remaining,"s")
    except Exception:
        print("No expiration date (Cookie expires when browser closes)")
