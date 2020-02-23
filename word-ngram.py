#!/usr/bin/python

import sys
import os
import math

#####################################################################
# Helper functions 
#####################################################################	

# function getNGrams(text, n)
# 	returns all phrases of length n words in text
def getNGrams(text, n):
	ngrams = []
	textList = text.split()
	
	i = 1

	while i <= (len(textList) - n + 1):
		ngram = " ".join(textList[i:i + n])
		ngrams.append(ngram)
		i+= int(n/4)
	
	return ngrams
# end def getNGrams()

# function readTxtFile(filepath)
#	returns contents of text file as string
def readFile(filepath):
	fo = open(filepath)
	return fo.read()
# end def readTxtFile()

# function percentileThreshold(lst, pct)
def percentileThreshold(lst, pct):
    lst = sorted((lst))

    if len(lst) < 1:
            return None
    else:
            return lst[int(math.ceil(len(lst)*pct))]
# end def topPct()


#####################################################################
# Main Script 
#####################################################################	
path = sys.argv[1]	
targetfile = sys.argv[2] + ".txt"
specificity = int(sys.argv[3])
scoreThreshold = int(sys.argv[4])


filenames = os.listdir(path)

os.chdir(path)

files = {}
for filename in filenames:
	if filename.endswith("txt"):
		files.update({filename: getNGrams(str(readFile(filename)).replace("\r\n", " "), specificity)})

targetNGrams = getNGrams(str(readFile(targetfile)).replace("\r\n", " "), specificity)


matchedFiles = {}

for file1 in files.items():
	if (file1[0] != targetfile):
		matches = list(set(file1[1]) & set(targetNGrams))
		score = len(matches)
		if score >= scoreThreshold:
			matchedFiles.update({file1[0]: matches})
		#end if
	#end if
#end for

for file in matchedFiles.items():
	print "#####################################################################"
	print file[0]
	print "#####################################################################"
	for i, str in enumerate(file[1]):
		print str
	print ""
#end for 

print ""

