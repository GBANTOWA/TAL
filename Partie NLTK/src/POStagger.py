import sys
from nltk import pos_tag
from nltk import RegexpParser
from nltk.tokenize import word_tokenize

sys.stdout = open('pos_test.txt.pos.nltk', 'w')
f = open('pos_test.txt')

text = word_tokenize(f.read())
tokens_tag = pos_tag(text)

print('\n'.join(map(str,tokens_tag)).replace("(","").replace(")","").replace("\"'s\"","]").replace("\"n't\"","[").replace("'","").replace("]","'s").replace("[","n't").replace("\"","").replace(" ",'\t').replace("\t,","\t~").replace(",,","|").replace(",","").replace("|",",").replace("~",","))

sys.stdout.close()
