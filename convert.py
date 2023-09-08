#!/usr/bin/env python3

import sys
import os
from pytube import Playlist

def main():
    if len(sys.argv) != 3:
        print(f'USAGE: python3 {sys.argv[0]} <location> <playlistURL>')
        sys.exit(1)

    location = sys.argv[1]
    playlistURL = sys.argv[2]

    if not os.path.exists(location):
        print(f'ERROR: {location} could not be found')
        sys.exit(1)

    if not os.path.isdir(location):
        print(f'ERROR: {location} is not directory')
        sys.exit(1)

    playlist = Playlist(playlistURL)

    if len(playlist) == 0:
        print('ERROR: Could not find any songs in playlist.')
        print('If there are songs in the playlist check that the URL you have entered is correct, and that the playlist is not private.')
        sys.exit(1)

    for song in playlist.videos:
        print(f'Downloading {song.title}')
        path = song.streams.get_audio_only().download(location)
        name, ext = os.path.splitext(path)
        os.rename(path, f'{name}.mp3')

if __name__ == '__main__':
    main()
