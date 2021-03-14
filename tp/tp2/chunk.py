import nltk
import sys
from nltk import pos_tag
from nltk import RegexpParser
from nltk.tokenize import word_tokenize
from grammar import grammarR

sys.stdout = open('wsj_0010_sample.txt.chk.nltk', 'w')
f = open('wsj_0010_sample.txt')

text = word_tokenize(f.read())
tokens_tag = pos_tag(text)

for rule in grammarR:
	cp = RegexpParser(rule)

output = cp.parse(tokens_tag)

print(output)
output.draw()

sys.stdout.close()




