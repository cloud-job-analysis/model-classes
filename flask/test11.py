import requests
import json

fp1 = 'flask/fp1.txt'

r11 = requests.get('http://127.0.0.1:5000/timsort?fpath=' + fp1)

