import requests
import json

fp5 = 'fp5.txt'
r55 = requests.get('http://127.0.0.1:5000/wordcount?fpath=' + fp5)
