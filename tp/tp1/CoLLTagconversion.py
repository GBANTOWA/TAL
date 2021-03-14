#****************************************************************
#
# CoNLLTagconvertion.py - the extraction of information after named entity tagging
#
# Author: Yawo Adufu
#
# University of Paris-Saclay. 2021.03
#
#****************************************************************

#================================================================
#
# Import modules.
#
#================================================================

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "libs")))
import getopt


opts, args = getopt.getopt(sys.argv[1:], "")
for opt in opts:
  print opt
if len(args) != 2:
  print g_sInformation
  sys.exit(1)
sFirstfile = args[0]
sResult = args[1]
if not os.path.exists(sFirstfile):
  print "Candidate file %s does not exist." % sFirstfile
  sys.exit(1)





#================================================================
#
# Creation of the dictionnary containing all the named entity found in the file
#
#================================================================
namedTagsFile = open(sFirstfile, "r")
resultFile = open(sResult, "w")
ned = {}
nbWord = 0
previousTag = ""
sentence = ""
for line in namedTagsFile:
    data = line.split()
    for wordandtag in data:
        nbWord += 1
        wordtag = wordandtag.split('/')
        if wordtag[1] != 'O': 
            if wordtag[1] == previousTag and wordtag[1] == "PERSON" :
               previousTag = wordtag[1]
               wordtag[1] = "I-PERS"
            else :
                if wordtag[1] == previousTag and wordtag[1] == "ORGANIZATION" :
                    previousTag = wordtag[1]
                    wordtag[1] = "I-ORG"
                else :            
                    if wordtag[1] == previousTag and wordtag[1] == "LOCATION" :
                        previousTag = wordtag[1]
                        wordtag[1] = "I-LOC"
                    else :    
                        if wordtag[1] == previousTag and wordtag[1] == "MISCELLANEOUS" :
                            previousTag = wordtag[1]
                            wordtag[1] = "I-MISC"
                        else :
                            if wordtag[1] != previousTag and wordtag[1] == "PERSON" :
                               previousTag = wordtag[1]
                               wordtag[1] = "B-PERS"
                            else :    
                                if wordtag[1] != previousTag and wordtag[1] == "ORGANIZATION" :
                                   previousTag = wordtag[1]
                                   wordtag[1] = "B-ORG"
                                else :
                                    if wordtag[1] != previousTag and wordtag[1] == "LOCATION" :
                                       previousTag = wordtag[1]
                                       wordtag[1] = "B-LOC"
                                    else :
                                        if wordtag[1] != previousTag and wordtag[1] == "MISCELLANEAOUS" :
                                           previousTag = wordtag[1]
                                           wordtag[1] = "B-MISC"
        sentence = sentence + wordtag[0]+"/"+wordtag[1] + " " 
    sentence = sentence[:-1]
    resultFile.write(sentence + "\n")
    sentence = ""
    




namedTagsFile.close()
resultFile.close()
#================================================================
#
# Swapping of the things
#
#================================================================

for element in ned:
    print(element )
    print(ned[element])

