#****************************************************************
#
# afterPosTaggeruniverssaltag.py - the swapping from Peen Treebank tags to universal tags after postagging   
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
# Creation of the dictionnary based on the file POSTags_PTB_Universal_Linux
#
#================================================================
universalTagsFile = open("POSTags_PTB_Universal_Linux.txt", "r")
tagDictionnary = {}
for line in universalTagsFile:
    tag = line.split()
    tagDictionnary[tag[0]] = tag[1]

universalTagsFile.close()
#================================================================
#
# Swapping of the things
#
#================================================================

fichierAConvertir1 = open(sFirstfile, "r")

fichierConverti1 = open( sResult , "w")

stringConversionFichier1 = ""


for line in fichierAConvertir1:
    data = line.split()
    for wordandtag in data:
        word_and_tag = wordandtag.split("_")
        word_and_tag[1] = tagDictionnary[word_and_tag[1]]
        wordandtagUniversal = word_and_tag[0] + "_" + word_and_tag[1]   
        stringConversionFichier1 = stringConversionFichier1 + wordandtagUniversal + " "
    stringConversionFichier1 = stringConversionFichier1[:-1]
    fichierConverti1.write(stringConversionFichier1 + "\n")
    stringConversionFichier1 = ""       




fichierAConvertir1.close()
fichierConverti1.close()
