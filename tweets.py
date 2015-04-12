import requests
import urllib2
from requests.exceptions import HTTPError
import re
import color

class Tweets:
	def __init__(self):
		color.load()

	def download_tweets(self, name):
		name = name.lower()
		request_url = "http://greptweet.com/f/"+name
		r = requests.get(request_url)
		if str(r.status_code) == "200":
			print "request success"
			print "getting tweets"
			for i in range(0,5):
				try:
					tweet_txt = urllib2.urlopen("http://greptweet.com/u/"+name+"/"+name+".txt")
					output = open('tweets/'+name+".txt",'w')
					output.write(tweet_txt.read())
					output.close()
					break
				except urllib2.HTTPError as e:
					print "retry("+str(i+1)+")"
		else:
			print "request tweets failed, please retry."

	def is_ascii(self, s):
		return all(ord(c) < 128 for c in s)

	def get_recent_tweets(self, name):
		text = ""
		with open("tweets/"+name+".txt") as tweet_file:
			lines = tweet_file.readlines()
			for i in range(0,50):
				if i < len(lines):
					content = lines[i].split("|")[2]
					content = re.sub(r'^https|http?:\/\/.*[\r\n]*', '', content, flags=re.MULTILINE)
					content = [c.lower() for c in content if self.is_ascii(c)]
					content = ''.join(content)
					text += (" "+content)
		return text

	def user_to_color(self, name):
		self.download_tweets(name) 
		return color.process(self.get_recent_tweets(name))