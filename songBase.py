import os
import pprint
import random
from random import randint

class Songbase:
	_base = {}
	def __init__(self):
		'''
		for dirnames in os.walk('./list'):
			for subdirname in dirnames:
				print subdirname
		'''
		pp = pprint.PrettyPrinter(indent=4)
		type_list = [d for d in os.listdir('list/') if not d.startswith('.')]
		for t in type_list:
			self._base[t] = {}
			song_list = [d for d in os.listdir('list/'+t+'/') if not d.startswith('.')]
			for s in song_list:
				self._base[t][s] = []
				with open('list/'+t+'/'+s, "r") as ins:
					for line in ins:
						self._base[t][s].append(line.strip())
		#pp.pprint(self._base)

	def get_size(self):
		count = 0;
		for t in self._base:
			for l in self._base[t]:
				count = count + len(self._base[t][l])
		return count;

	def get_song(self, color, country, age, tracks):
		song_type_list = self.color_to_type(color);
		cur_type = song_type_list[randint(0,len(song_type_list)-1)]
		song_dict = self._base[cur_type]
		song_list = song_dict[random.choice(song_dict.keys())]
		random_song = song_list[randint(0,len(song_list)-1)]
		return random_song

	def color_to_type(self, color):
		type_list = []
		if color == 'white':
			type_list = ['dinner','sleep','soul']
		elif color == 'black':
			type_list = ['metal','rock','workout']
		elif color == 'red':
			type_list =  ['rock','workout','party','pop']
		elif color == 'green':
			type_list = ['romance','soul']
		elif color == 'yellow':
			type_list = ['focus','travel']
		elif color == 'blue':
			type_list = ['focus','sleep','jazz']
		elif color == 'brown':
			type_list = ['party','dinner','blues']
		elif color == 'pink':
			type_list = ['romance','country']
		elif color == 'purple':
			type_list = ['party','soul','travel']
		elif color == 'orange':
			type_list = ['workout','travel','pop','rock']
		elif color == 'grey':
			type_list = ['blues','travel','rock','focus']
		else:
			type_list = ['blues','classical','country','dinner','focus','jazz','metal','party','pop','rock','romance','sleep','soul','travel','workout']
		return type_list

	def process_age(self, age, lst):
		if age < 30:
			lst = [ x for x in lst if x == 'blues' or x == 'jazz' ]
			lst.append('pop')
		return lst
	def add_additional(self, more, lst):
		for t in more:
			lst.append(t)
		return lst