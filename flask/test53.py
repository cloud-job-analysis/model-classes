import requests
import json

fp5 = 'flask/fp5.txt'
r53 = requests.get('http://127.0.0.1:5000/insertionsort?fpath=' + fp5)
