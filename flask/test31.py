import requests
import json

fp3 = 'fp3.txt' 
r31 = requests.get('http://127.0.0.1:5000/timsort?fpath=' + fp3)
