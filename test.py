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


from nltk.parse.stanford import StanfordParser
path_to_jar = 'stanford-parser-full-2016-10-31/stanford-parser.jar'
path_to_models_jar = 'stanford-parser-full-2016-10-31/stanford-parser-3.7.0-models.jar'
parser = StanfordParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)



result = parser.raw_parse('First take out your jumper cables and then place both vehicles in park and shut off the engine. Attach the clip to the positive terminal of your battery and then attach the other red clip to the positive terminal of the other battery. Attach one of the black clip to the negative terminal of the battery. Attach the last black clip to any metal surface in the car that is not a battery. start the working car and let it run for few minutes. Try to start your car. Remove the clips in the reverse order. ')

final = list(result)
print final[0].pretty_print()
#print final[0].treepositions()
#print list(final[0].treepositions()[2])
#print final[0][0, 1, 0, 0, 0].label()
#print final[0][final[0].treepositions()[i]] i is the iterator that can go through all elements of the tuple
#print final[0][0, 1, 0, 0].label() == "VB"
# for i in range(len(final[0].treepositions())):
# 	try:
# 		if final[0][final[0].treepositions()[i]].label() == "V":
# 			for j in range(i+1, len(final[0].treepositions())):

# 	except:
# 		print final[0][final[0].treepositions()[i]]
# print len(final[0].treepositions())


