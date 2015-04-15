import tweets
import songBase
import webbrowser
import fb


t = tweets.Tweets()
base = songBase.Songbase()


def init():
	global my_name
	global my_color
	my_name = raw_input('Enter your twitter name: ')
	my_color = t.user_to_color(my_name)
	print "Song base size: "+str(base.get_size())
	print "=========================="
	print "Your color is: "+my_color

def next_song():
	global my_color
	global my_url
	my_url = base.get_song(my_color,"SG",22,[])
	print "Current song:  "+my_url
	print "1. Next song"
	print "2. Like this song"
	webbrowser.open(my_url)

def like_song():
	global my_color
	global my_url
	fb.postToFirebase(my_color, "unknownType", my_url)
	print "Liked this song"

init()
next_song()


op = int(raw_input(">> "))
while op != 3:
	if op == 1:
		next_song()
	elif op == 2:
		like_song()
	op = int(raw_input(">> "))

