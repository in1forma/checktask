import requests
host="www.appstankasappps.com"
url="https://"+host
req=requests.get(url)
print(req.text)
