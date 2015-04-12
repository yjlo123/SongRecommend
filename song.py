import spotipy

input_files = ['pop.txt']

for f in input_files:
  f = open(f)

  song_links = f.read().splitlines()
  spotify = spotipy.Spotify()
  songs = spotify.tracks(song_links)
  print songs

