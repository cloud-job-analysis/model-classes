import requests
import json

fp3 = 'fp3.txt' 
r35 = requests.get('http://127.0.0.1:5000/wordcount?fpath=' + fp3)
