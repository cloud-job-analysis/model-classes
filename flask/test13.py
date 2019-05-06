import requests
import json

fp1 = 'fp1.txt' 

r13 = requests.get('http://127.0.0.1:5000/insertionsort?fpath=' + fp1)
