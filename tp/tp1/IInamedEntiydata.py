#****************************************************************
#
# 2duniverssaltag.py - the extraction of information after named entity tagging
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
if len(args) != 1:
  print g_sInformation
  sys.exit(1)
sFirstfile = args[0]
if not os.path.exists(sFirstfile):
  print "Candidate file %s does not exist." % sFirstfile
  sys.exit(1)





#================================================================
#
# Creation of the dictionnary containing all the named entity found in the file
#
#================================================================
namedTagsFile = open(sFirstfile, "r")
ned = {}
nbWord = 0
for line in namedTagsFile:
    data = line.split()
    for wordandtag in data:
        nbWord += 1
        if wordandtag.split('/')[1] != 'O':               
            if wordandtag in ned: 
                ned[wordandtag] += 1
            else:  
                ned[wordandtag] = 1


namedTagsFile.close
#================================================================
#
# Swapping of the things
#
#================================================================

for element in ned:
    print(element )
    print(ned[element])

