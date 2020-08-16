#!/bin/python
import requests
import time
url = raw_input('Enter URL to Test:')
response = requests.get(url)
if response.status_code == 200:
    print('Success:')
elif response.status_code !=200:
    print('Failed: ')
