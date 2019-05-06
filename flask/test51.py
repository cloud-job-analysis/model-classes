import requests
import json

fp5 = 'flask/fp5.txt'
r51 = requests.get('http://127.0.0.1:5000/timsort?fpath=' + fp5)
