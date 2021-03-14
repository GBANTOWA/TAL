import nltk
import sys
from nltk import pos_tag
from nltk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from grammar import grammarR

sys.stdout = open('wsj_0010_sample.txt.ne.nltk', 'w')
f = open('wsj_0010_sample.txt')

text = word_tokenize(f.read())
tokens_tag = pos_tag(text)

train_text = state_union.raw("2005-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(f.read())

tagged = nltk.pos_tag(text)
namedEnt = nltk.ne_chunk(tagged, binary=False)

print(namedEnt)
namedEnt.draw()

sys.stdout.close()




