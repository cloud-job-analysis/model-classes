import requests
import json

fp3 = 'flask/fp3.txt' 
r34 = requests.get('http://127.0.0.1:5000/bubblesort?fpath=' + fp3)
