import requests
import json

fp3 = 'flask/fp3.txt' 
r33 = requests.get('http://127.0.0.1:5000/insertionsort?fpath=' + fp3)
