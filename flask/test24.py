import requests
import json

fp2 = 'flask/fp2.txt' 
r24 = requests.get('http://127.0.0.1:5000/bubblesort?fpath=' + fp2)
