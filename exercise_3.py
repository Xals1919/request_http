import requests

url = "https://api.stackexchange.com/2.3/search?todate=1689897600&order=desc&max=1689984000&sort=activity&tagged=" \
      "Python&site=stackoverflow"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()

url = data['items']
for name in url:
    print(name['title'])
