import requests
import records
import passlib

r = requests.get("http://google.com")
print(r.status_code)