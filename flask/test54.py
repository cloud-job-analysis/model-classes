import requests
import json

fp5 = 'flask/fp5.txt'
r54 = requests.get('http://127.0.0.1:5000/bubblesort?fpath=' + fp5)
