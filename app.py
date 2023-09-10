#!/usr/bin/env python3

import sys
import os
from pytube import Playlist
from flask import Flask, request, render_template, send_file
from shutil import make_archive, move

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/download')
def download():
    playlistURL = request.form['text']
    playlist = Playlist(playlistURL)

    clear_data()
    for song in playlist.videos:
        print(f'Downloading {song.title}')
        path = song.streams.get_audio_only().download('data')
        name, _ = os.path.splitext(path)
        os.rename(path, f'{name}.mp3')

    archive = make_archive('music', 'zip', os.path.dirname(path))
    move(archive, './data')
    return send_file('./data/music.zip')

def clear_data():
    [ os.remove(os.path.join(os.path.curdir, 'data', file)) for file in os.listdir('./data') ]
