import requests
TOKEN = "ce6f97de53a2d4c3e48ba0a0ac6c2234aaa45ccb"
URL = 'https://api-ssl.bitly.com/v4/shorten'

HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}

data = '{ "long_url": "https://bitly.com/"}'
x = data[:15]+"https://www.google.com/"+data[-2:]
new_data = x

third_data = '{ "long_url": "https://dev.bitly.com"}'


response = requests.post(url=URL, headers=HEADERS, data=x).json()

print(response)
print(new_data)
print(third_data)