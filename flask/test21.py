import requests
import json

fp2 = 'fp2.txt' 
r21 = requests.get('http://127.0.0.1:5000/timsort?fpath=' + fp2)
