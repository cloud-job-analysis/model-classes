import requests
import json

fp4 = 'fp4.txt' 
r43 = requests.get('http://127.0.0.1:5000/insertionsort?fpath=' + fp4)
