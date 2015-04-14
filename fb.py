from firebase import firebase
import urllib2
import socket

firebase = firebase.FirebaseApplication('https://cs4242.firebaseio.com', None)
'''
result = firebase.get('/data', None)
print result
'''

def postToFirebase(my_color, my_type, my_song):
	my_ip = urllib2.urlopen('http://ip.42.pl/raw').read()
	firebase.post('/data', {'ip': my_ip, 'color': my_color, 'type': my_type, 'song': my_song})
'''
my_color = "red"
my_type = "2"
my_song = "123"
postToFirebase(my_color, my_type, my_song)
'''