#!/usr/bin/env python3

from flask import Flask, request, render_template, send_file
from download import download

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/convert')
def convert():
    playlistURL = request.form['text']
    download(playlistURL)
    return send_file('./data/music.zip')
