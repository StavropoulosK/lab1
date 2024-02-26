import requests
import time

url= input("Give url: ")   

response=requests.get(url)
headers=response.headers

print("Τα headers είναι: \n\n")
for key,value in headers.items():
    print(key,":",value,"\n")

print("\nΤο λογισμικό που χρησιμοποιεί ο εξυπηρετητής (ο web server) για να απαντήσει στο αίτημα είναι: ",headers['Server'])

if(len(response.cookies)==0):print("Η σελίδα δεν χρησιμοποιεί cookies")
else:
    print("Η σελίδα  χρησιμοποιεί cookies")

for cookie in response.cookies:

    print("Cookie name: ", cookie.name)

    if(cookie.expires!=None):

        remaining=   cookie.expires- int(time.time())
        print("Time left to expire: ", remaining,"s")

    else:

        print("To cookie tha sbisti otan klisi o browser")


