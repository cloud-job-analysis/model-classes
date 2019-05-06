# ./app.py

from flask import Flask, render_template, request, jsonify
from random import *
from time import * 

import json
import time

# create flask app
app = Flask(__name__)

# index route, shows index.html view
@app.route('/')
def index():
    data = {"time": time.time()}
    return jsonify(data)

# endpoint for simple file IO
# return file handle to work with
@app.route('/createemptyfile', methods=['GET'])
def createEmptyFile():
    fpath = request.args.get('fpath')
    f = open(fpath, 'w+')
    data = {'id' : f}
    return jsonify(data)

# endpoint for writing to file
# takes in file handle
@app.route('/writetofile', methods=['GET'])
def writeToFile():
    f = request.args.get('fpath')
    info = request.args.get('info')
    f.write(info)
    data = {'id' : f}
    return jsonify(data)

# endpoint for creating to file, writing to it and returning information
# takes in file path
@app.route('/filework', methods=['GET'])
def fileWork():
    fpath = request.args.get('fpath')
    info = request.args.get('info')
    fp = open(fpath, 'w+')
    fp.write(info)
    fp.close()
    data = {'id' : True}
    return jsonify(data)

def return_wordcount(fpath):
    f = open(fpath, 'r')
    word_count = {}
    for line in f.readlines():
        for word in line.split():
            try:
                word_count[word] = 1
            except:
                word_count += 1
    return word_count

@app.route('/timsort', methods=['GET'])
def timsort():
    print('request accepted timsort')
    fpath = request.args.get('fpath')
    arr_d = return_wordcount(fpath)
    arr = list(arr_d.keys())
    arr1 = arr.sort()
    return jsonify(arr1)

@app.route('/bogosort', methods=['GET'])
def bogosort():
    print('request accepted bogosort')
    fpath = request.args.get('fpath')
    fp = open(fpath)
    arr = fp.readlines()
    fp.close()
    x = []
    for a in arr:
        x.append(int(a))
    while not inorder(x):
        shuffle(x)
    return jsonify(x)

def inorder(x):
    i = 0
    j = len(x)
    while i + 1 < j:
        if x[i] > x[i + 1]:
            return False
        i += 1
    return True

@app.route('/insertionsort', methods=['GET'])
def insertionsort():
    print('request accepted insertionsort')
    fpath = request.args.get('fpath')
    arr_d = return_wordcount(fpath)
    arr = list(arr_d.keys())
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key
    return jsonify(arr)

@app.route('/bubblesort', methods=['GET'])
def bubblesort():
    print('request accepted bubblesort')
    fpath = request.args.get('fpath')
    arr_d = return_wordcount(fpath)
    arr = list(arr_d.keys())
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return jsonify(arr)

@app.route('/wordcount', methods=['GET'])
def wordcount():
    print('request accepted wordcount')
    fpath = request.args.get('fpath')
    f = open(fpath, 'r')
    word_count = {}
    for line in f.readlines():
        for word in line.split():
            try:
                word_count[word] = 1
            except:
                word_count += 1
    return jsonify(word_count)

# run Flask app in debug mode
app.run(debug=True)