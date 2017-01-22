import nltk
from nltk.parse.stanford import StanfordParser
path_to_jar = 'stanford-parser-full-2016-10-31/stanford-parser.jar'
path_to_models_jar = 'stanford-parser-full-2016-10-31/stanford-parser-3.7.0-models.jar'
parser = StanfordParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

# text_doc2 = 'Visit the JDK download page. Open your web browser and visit oracle.com/downloads/index.html.' + ' Double-click the downloaded installer. The installer is in .dmg format. Double-clicking it will open the installation interface.'+' Follow the prompts to install the JDK. You\'ll be asked to enter your administrator password before installation can proceed.'

text_doc = 'First take out your jumper cables and then place both vehicles in park and shut off the engine. Attach the clip to the positive terminal of your battery and then attach the other red clip to the positive terminal of the other battery. Attach one of the black clip to the negative terminal of the battery. Attach the other last black clip to any metal surface in the car that is not a battery. start the working car and let it run for few minutes. Try to start your car. Remove the clips in the reverse order.'
sents = nltk.sent_tokenize(text_doc)
sents = nltk.sent_tokenize(text_doc2)

text_doc2 = 'Play bass guitar at apppropriate vol, slightly higher. Then start the electric guitar intro. After that bring in improvisation from keyboard.'
text_doc3 = 'Open terminal. Type pip install pygame and press enter. After completion, get to python prompt. Test by importing.'

sent2 = text_doc2.split(".")
sent3 = text_doc3.split(".")

sent2 = sent2[:len(sent2)-1]
sent3 = sent3[:len(sent3)-1]

sents = [sent2, sent3]

# print ("Sent: ", sents)
# print ("Sent2: ", sent2)
# print ("Sent3: ", sent3)

# c_CC = c_CD = c_DT = c_EX = c_FW = c_IN = c_IN = c_JJ = c_JJR = c_JJS = 0
# c_LS = c_MD = c_NN = c_NNS = c_NNP = c_NNPS = c_PDT = c_POS = c_PRP = 0
# c_PRPD = c_RB = c_RBR = c_RBS = c_RP = c_SYM = c_TO = c_UH = c_VB = 0
# c_VBD = c_VBG = c_VBN = c_VBP = c_VBZ = c_WDT = c_WP = c_WPD = c_WRB = 0

# c_{POS} -> denotes count_{POS}
# $ sign at the end of POS is translated with {pos}D


for outer in sents:
    for sent in outer:
        result = parser.raw_parse(sent)
        final = list(result)
        my_list = []
        flag2 = flag1 = 0
        string = ""
        leaves = []
        
        par_to_chrn = {}
        lis = sorted(final[0].treepositions())
        f = final[0]
        
        for i in range(len(final[0].treepositions())):
            try:
                par_to_chrn[f[lis[i]].label()]
                par_to_chrn[f[lis[i]].label()+str()]
#             try:
#                 if final[0][final[0].treepositions()[i]].label() == "VB":
#                     #leaves = final[0][final[0].treepositions()[i].leaves()]
#                     my_list.append(string)
#                     string = ''
#                     string += final[0][final[0].treepositions()[i+1]]
#                     string += " "

#                 elif final[0][final[0].treepositions()[i]].label() == "IN":
#                     string += " "
#                     string += final[0][final[0].treepositions()[i+1]]

#                 elif final[0][final[0].treepositions()[i]].label() == "RP":
#                     string += " "
#                     string += final[0][final[0].treepositions()[i+1]]

#                 elif final[0][final[0].treepositions()[i]].label() == "JJ":
#                     string += " "
#                     string += final[0][final[0].treepositions()[i+1]]

#                 elif final[0][final[0].treepositions()[i]].label() == "NN":
#                     string += " "
#                     string += final[0][final[0].treepositions()[i+1]]


#                 elif final[0][final[0].treepositions()[i]].label() == "NNS":
#                     string += " "
#                     string += final[0][final[0].treepositions()[i+1]]

#             except:
#                 a = 1

        if string != "":
            my_list.append(string)
        del my_list[0]
        print (my_list)

# 'First take out your jumper cables.' 
# 'and then place both vehicles in park'
# 'and shut off the engine. '
# 'Attach the clip to the positive terminal of your battery'
# 'and then attach the other red clip to the positive terminal of the other battery.' 
# 'Attach one of the black clip to the negative terminal of the battery.'
# 'Attach the other last black clip to any metal surface in the car that is not a battery.'
# 'start the working car and let it run for few minutes.'
# 'Try to start your car. Remove the clips in the reverse order.'