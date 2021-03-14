#****************************************************************
#
# extractionPos_test.py - the extraction of the sentences from the annoted corpus
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
sResultat = args[1]
if not os.path.exists(sCandidate):
  print "Candidate file %s does not exist." % sCandidate
  sys.exit(1)




fichierAConvertir = open(sCandidate, "r")
fichierConverti = open(sResultat, "w")
stringConversion = ""

for line in fichierAConvertir:
    data = line.split("\t")
    if len(data) != 1 :
        stringConversion =  stringConversion + data[0] + " "
    if len(data) == 1  or (len(data) == 3 and data[0] == "" and data[1] == ""):
        stringConversion = stringConversion[:-1]
        fichierConverti.write(stringConversion + "\n")
        stringConversion = ""


fichierAConvertir.close()
fichierConverti.close()
