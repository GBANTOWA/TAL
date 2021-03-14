#****************************************************************
#
# universsaltag.py - the swapping from Peen Treebank tags to universal tags.
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
sCandidate = args[0]
sResult = args[1]
if not os.path.exists(sCandidate):
  print "Candidate file %s does not exist." % sCandidate
  sys.exit(1)





#================================================================
#
# Creation of the dictionnary based on the file POSTags_PTB_Universal_Linux
#
#================================================================
PTBTagsFile = open("POSTags_LIMA_PTB_Linux.txt", "r")
tagDictionnaryLima_PTB = {}
for line in PTBTagsFile:
    tag = line.split()
    tagDictionnaryLima_PTB[tag[0]+"\n"] = tag[1]

PTBTagsFile.close()





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

fichierAConvertir = open(sCandidate, "r")

fichierConverti = open( sResult , "w")



for line in fichierAConvertir:
    data = line.split("\t")
    if len(data) != 1 :
        data[1] = tagDictionnaryLima_PTB[data[1]]
        data[1] = tagDictionnary[data[1]]
        stringConversion =  data[0]+ "\t" + data[1]
        fichierConverti.write(stringConversion + "\n")
        stringConversion = ""
    if len(data) == 1  or (len(data) == 3 and data[0] == "" and data[1] == ""):
        fichierConverti.write("\n")

     





fichierAConvertir.close()
fichierConverti.close()

