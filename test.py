import requests

headers = {'header': 'application/x-www-form-urlencoded'}

data = 'grant_type=client_credentials&client_id=A43D2E2D-E53B-40F8-92A5-B92698FE18B1&client_secret=41BF8A2F-E44C-44B3-9849-C6C4957380B5'

response = requests.post('https://api.tcgplayer.com/token', headers=headers, data=data)

print(response.json())