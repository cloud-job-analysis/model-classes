import requests
import json

fp4 = 'flask/fp4.txt' 
r41 = requests.get('http://127.0.0.1:5000/timsort?fpath=' + fp4)
