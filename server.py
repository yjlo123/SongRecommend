from flask import Flask
from flask import *
import spotipy
import spotipy.util as util

app = Flask(__name__)

@app.route('/')
def index():
  token = request.args.get('token', '')
  output = ''
  if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
      track = item['track']
      output = output + track['name'] + ' '

  return output

@app.route('/spotify')
def spotify_login(username=None):
  scope = 'user-library-read user-follow-read user-read-private user-read-birthdate user-read-email'
  token = util.prompt_for_user_token(scope)
  return redirect(url_for('index', token = token))



if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=8080)
