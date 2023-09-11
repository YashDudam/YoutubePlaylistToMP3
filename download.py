#!/usr/bin/env python3

import os
from pytube import Playlist
from shutil import make_archive, move

from data import clear, mkdata

def download(url):
    playlist = Playlist(url)

    mkdata()
    clear()
    for song in playlist.videos:
        try:
            print(f'Downloading {song.title}')
            path = song.streams.get_audio_only().download('data')
            name, _ = os.path.splitext(path)
            os.rename(path, f'{name}.mp3')
        except:
            print(f'Failed to download {song.title} :(')

    archive = make_archive('music', 'zip', os.path.dirname(path))
    clear()
    move(archive, './data')
