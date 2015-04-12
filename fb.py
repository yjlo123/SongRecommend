from firebase import firebase
import socket

firebase = firebase.FirebaseApplication('https://cs4242.firebaseio.com', None)
'''
result = firebase.get('/data', None)
print result
'''

def postToFirebase(my_color, my_type, my_song):
	my_ip = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
	firebase.post('/data', {'ip': my_ip, 'color': my_color, 'type': my_type, 'song': my_song})
'''
my_color = "red"
my_type = "2"
my_song = "123"
postToFirebase(my_color, my_type, my_song)
'''