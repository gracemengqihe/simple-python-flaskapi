import requests
import json 

response = requests.get('https://api.stackexchange.com//2.2/answers?order=desc&sort=activity&site=stackoverflow')


for data in response.json()['items']:
    print(data)
    break
