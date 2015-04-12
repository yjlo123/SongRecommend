from flask import Flask
from flask import *
import spotipy
import spotipy.util as util
import os

os.environ['SPOTIPY_CLIENT_ID']     = '80d72b0f268d4e7db2ffd1e70d79be31'
os.environ['SPOTIPY_CLIENT_SECRET'] = '57f4a3f15b7a4399b3c6e6acab190221'
os.environ['SPOTIPY_REDIRECT_URI']  = 'http://localhost:8080/'

app = Flask(__name__)

@app.route('/')
def index():
  token = request.args.get('token', '')
  if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    profile = sp.me()
  else:
    results = None
    profile = None
  twitter = request.args.get('twitter', '')

  return render_template('index.html', token=token, results=results, profile=profile, twitter=twitter)

@app.route('/spotify')
def spotify_login(username=None):
  scope = 'user-library-read user-follow-read user-read-private user-read-birthdate user-read-email'
  token = util.prompt_for_user_token(scope)
  return redirect(url_for('index', token = token))

@app.route('/twitter')
def twitter_login():
  pass


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=8080)
