# from nltk.parse.stanford import StanfordDependencyParser
# path1 = 'Users/Rouzbeh/Downloads/Hackathon/stanford-parser-full-2015-04-20/stanford-parser.jar'
# path2 = 'Users/Rouzbeh/Downloads/Hackathon/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar'
# dependency_parser = StanfordDependencyParser(path_to_jar=path1, path_to_models_jar=path2)

# from nltk.parse.stanford import StanfordParser
# # list(parser.raw_parse("the quick brown fox jumps over the lazy dog"))
# from nltk.internals import find_jars_within_path
# jar = 'Users/Rouzbeh/Downloads/Hackathon/stanford-parser-full-2015-04-20/stanford-parser.jar'
# model = 'Users/Rouzbeh/Downloads/Hackathon/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar'
# parser=StanfordParser(model,jar)

# import os
# from nltk.parse import stanford
# os.environ['STANFORD_PARSER'] = 'Users/Rouzbeh/Downloads/Hackathon/stanford-parser-full-2015-04-20/stanford-parser.jar'
# os.environ['STANFORD_MODELS'] = 'Users/Rouzbeh/Downloads/Hackathon/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar'
# parser = stanford.StanfordParser(model_path="Users/Rouzbeh/Downloads/Hackathon/englishPCFG.ser.gz")
# sentences = parser.raw_parse_sents(("Hello, My name is Melroy.", "What is your name?"))
# print sentences

from graphviz import Digraph

from nltk.parse.stanford import StanfordParser
path_to_jar = 'stanford-parser-full-2016-10-31/stanford-parser.jar'
path_to_models_jar = 'stanford-parser-full-2016-10-31/stanford-parser-3.7.0-models.jar'
parser = StanfordParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)


result = parser.raw_parse('First take out your jumper cables and then place both vehicles in park and shut off the engine.')

final = list(result)
print final[0].pretty_print()
#print final[0].treepositions()
#print list(final[0].treepositions()[2])
#print final[0][0, 1, 0, 0, 0].label()
#print final[0][final[0].treepositions()[i]] i is the iterator that can go through all elements of the tuple
#print final[0][0, 1, 0, 0].label() == "VB"
my_list = []
flag2 = flag1 = 0
string = ""
for i in range(len(final[0].treepositions())):
	try:
		if final[0][final[0].treepositions()[i]].label() == "VB":
			print 1
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
print my_list

dot = Digraph(comment='The Round Table')
dot.node('A', my_list[0])
dot.node('B', my_list[1])
dot.node('C', my_list[2])
dot.edges(['AB','BC'])

dot.render('test-output/round-table.gv', view=True)


