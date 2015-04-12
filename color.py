import nltk
import pickle
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import operator

def preprocess():
	porter = nltk.PorterStemmer()
	train = []
	colour_dict = {}
	with open("NRC_color_lexicon.txt", "r") as ins:
		#for i in range(0,30):
		#line = ins.readline()
		for line in ins:
			tokens = line.split()
			word = tokens[0].split("--")[0]
			word = porter.stem(word)
			color = tokens[-3].split("=")[1]
			if color != "None":
				#print word+" "+color
				#train.append((word, color))
				#color_dict[color] += (" "+word)
				colour_dict[word] = color
	return colour_dict

def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def load_object(filename):
	with open(filename, 'rb') as input:
		return pickle.load(input)

def getColorFromText(color_dict, str):
	color_count = {"white":0, "black":0, "red":0, "green":0, "yellow":0, "blue":0, "brown":0, "pink":0, "purple":0, "orange":0, "grey":0}
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(str)
	tokens = [w.lower() for w in tokens]
	filtered_words = [w for w in tokens if not w in stopwords.words('english')]
	porter = nltk.PorterStemmer()
	stemmed_words = [porter.stem(t) for t in filtered_words]
	for w in  stemmed_words:
		if w in color_dict:
			color_count[color_dict[w]] += 1
	print color_count
	return max(color_count.iteritems(), key=operator.itemgetter(1))[0]


color_dict = {}

def load():
	global color_dict
	print "loading..."
	color_dict = load_object("color_dictionary.data")

def generate():
	color_dict = preprocess()
	print "saving..."
	save_object(color_dict, "color_dictionary.data")

def process(text):
	global color_dict
	return getColorFromText(color_dict, text)
