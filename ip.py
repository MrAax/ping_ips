# gei ip information with python
import requests
import pprint
ip="8.8.8.8"
url=f"https://ipapi.co/{ip}/json/"
r=requests.get(url)
pprint.pprint(r.json())
