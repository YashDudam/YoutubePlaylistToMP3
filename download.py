#!/usr/bin/env python3

import os
from threading import Thread
from pytube import Playlist
from shutil import make_archive, move

from data import clear

# test URL https://www.youtube.com/playlist?list=PLk2ZBF-TwotrDkpQPLzOExgDqpi8xiyfu

def download(url):
    playlist = Playlist(url)
    download_threads = [ Thread(target=download_song, args=(song,)) for song in playlist.videos ]

    for thread in download_threads:
        thread.start()

    for thread in download_threads:
        thread.join()

    clear()
    file = make_archive(base_name='music', format='zip', root_dir='./data')
    move(file, 'data')

def download_song(song):
    try:
        print(f'Downloading {song.title}')
        path = song.streams.get_audio_only().download('data')
        name, _ = os.path.splitext(path)
        os.rename(path, f'{name}.mp3')
    except:
        print(f'Failed to download {song.title} :(')

