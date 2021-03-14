#****************************************************************
#
# 2bconversionStanford.py - the conversion to stanford pos ref program.
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
sCandidate = args[0]
if not os.path.exists(sCandidate):
  print "Candidate file %s does not exist." % sCandidate
  sys.exit(1)








fichierAConvertir = open(sCandidate, "r")
fichierConverti = open(sCandidate[:-3] + "stanford.ref", "w")

stringConversion = ""

for line in fichierAConvertir:
    data = line.split()
    stringConversion = stringConversion + data[0]+"_"+data[1]+" "
    if data[0]== ".":
        stringConversion = stringConversion[:-1]
        fichierConverti.write(stringConversion + "\n")
        stringConversion = ""


fichierAConvertir.close()
fichierConverti.close()
