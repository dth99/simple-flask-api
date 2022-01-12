# modules
import requests as rq
from datetime import datetime

#base url
BASE_URL = 'http://dth99.pythonanywhere.com/'
string=input()

#query/payload
payload={'input':string}

#calling aws public api
response = rq.get(BASE_URL,params=payload)

# json handling
json_values= response.json()
rq_input=json_values['input']
timestamp=json_values['timestamp']
character_c=json_values['character_count']

#priting data
print(f'Input is: {rq_input}')
print(f'Date is: {datetime.fromtimestamp(timestamp)}')
print(f'Character count is : {character_c}')