import os
import spotipy
import spotipy.util as util
from flask import Flask
from flask import *
from datetime import date
import datetime
import tweets
import fb
import songBase

os.environ['SPOTIPY_CLIENT_ID']     = '80d72b0f268d4e7db2ffd1e70d79be31'
os.environ['SPOTIPY_CLIENT_SECRET'] = '57f4a3f15b7a4399b3c6e6acab190221'
os.environ['SPOTIPY_REDIRECT_URI']  = 'http://localhost:8080/'

app = Flask(__name__)

def calculate_age(born):
  born = datetime.datetime.strptime(born, "%Y-%m-%d").date()
  today = date.today()
  return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

@app.route('/')
def index():
  token = request.args.get('token', '')

  twitter = request.args.get('twitter', '')
  if twitter:
    t = tweets.Tweets()
    color = t.user_to_color(twitter)
  else:
    color = None

  if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    profile = sp.current_user()
    base = songBase.Songbase()
    country = profile['country']
    age     = calculate_age(profile['birthdate'])
    song = base.get_song(color, country, age, [])
  else:
    results = None
    profile = None
    song    = None

  return render_template('index.html', token=token, results=results, profile=profile, twitter=twitter, color=color, song=song)

@app.route('/spotify')
def spotify_login(username=None):
  scope = 'user-library-read user-follow-read user-read-private user-read-birthdate user-read-email'
  token = util.prompt_for_user_token('new', scope)
  twitter = request.args.get('twitter', '')
  return redirect(url_for('index', token = token, twitter = twitter))

@app.route('/like', methods=[ 'POST' ])
def like():
  color = request.form['color']
  song = request.form['song']
  fb.postToFirebase(color, "unknownType", song)
  return 'Added song to color' 

@app.route('/home')
def home():
  return render_template('home.html')

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=8080)
