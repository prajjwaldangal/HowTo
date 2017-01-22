from graphviz import Digraph
import nltk
from nltk.parse.stanford import StanfordParser
from string import ascii_lowercase

path_to_jar = 'stanford-parser-full-2016-10-31/stanford-parser.jar'
path_to_models_jar = 'stanford-parser-full-2016-10-31/stanford-parser-3.7.0-models.jar'
parser = StanfordParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

print "The program is running, please wait !"
text_doc = 'Attend every class sessions. Pay attention and take good notes. Review your notes after every class. Always turn homeworks on time. Study for exam a week in advance. Get a enough sleep and eat a good meal before taking the exam. Good luck with the exam and get ready for the parties.'
sents = nltk.sent_tokenize(text_doc)
all_list = []
for sent in sents:
	result = parser.raw_parse(sent)
	final = list(result)
	#print final[0].pretty_print()
	my_list = []
	flag2 = flag1 = 0
	string = ""
	for i in range(len(final[0].treepositions())):
		try:
			if final[0][final[0].treepositions()[i]].label() == "VB":
				my_list.append(string)
				string = ''
				string += final[0][final[0].treepositions()[i+1]]
				string += " "

			elif final[0][final[0].treepositions()[i]].label() == "IN":
				string += " "
				string += final[0][final[0].treepositions()[i+1]]

			elif final[0][final[0].treepositions()[i]].label() == "RP":
				string += " "
				string += final[0][final[0].treepositions()[i+1]]

			elif final[0][final[0].treepositions()[i]].label() == "JJ":
				string += " "
				string += final[0][final[0].treepositions()[i+1]]

			elif final[0][final[0].treepositions()[i]].label() == "NN":
				string += " "
				string += final[0][final[0].treepositions()[i+1]]
				

			elif  final[0][final[0].treepositions()[i]].label() == "NNS":
				string += " "
				string += final[0][final[0].treepositions()[i+1]]
				
		except:
			a = 1

	if string != "":
		my_list.append(string)
	del my_list[0]
	all_list.append(my_list)
	#print my_list

dot = Digraph(comment='The Round Table')
chars = []
index = 0
for alpha in ascii_lowercase:
	chars.append(alpha)
edge_list = []
for item in reversed(all_list):
	local_char = []
	for elem in item:
		local_char.append(chars[index])
		dot.node(chars[index], elem)
		index += 1
	i = 0
	
	while i < (len (local_char) -1):
		edge_list.append(local_char[i]+local_char[i+1])
		i +=1 
dot.edges(edge_list)
	# dot = Digraph(comment='The Round Table')
	# dot.node('A', my_list[0])
	# dot.node('B', my_list[1])
	# dot.node('C', my_list[2])
	# dot.edges(['AB','BC'])
dot.graph_attr['rankdir'] = 'LR'
dot.graph_attr['color'] = 'red'
dot.render('test-output/round-table.gv', view=True)


