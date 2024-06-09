'''import requests

req=requests.get("https://kalob.io")

print(req.status_code)'''

'''import requests
import time
while True:
    req=requests.get("https://courses.codingforeverybody.com")
    print(req.status_code)
    if req.status_code != 200:
        pass
    time.sleep(3)'''

import requests
req = requests.get("https://swapi.dev/api/people/2/")
person = req.json()
print(f"Name is \t{person['name']}")
print(f"Birth year is \t\t{person['birth_year']}")

for film in person['films']:
    req = requests.get(film)
    film = req.json()
    print("Film is:",film['title'])
