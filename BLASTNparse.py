#!/usr/bin/env python3

# encoding: utf8
# author: Anam Ahsan

import re
import sys

#Open file with given filepath
my_file = open("/export/home/aahsan4/example_blast.txt")

#Read singleline of open file and stores in new variable
my_entries = my_file.readline()

#Function to extract accession, score and length of first 10 alignments
def alignments():
    max = 0
    #Opens file to extract alignments
    for line in open("/export/home/aahsan4/example_blast.txt"): 
        #Extracts accession by finding match and stores to new variable
        if line.startswith('>'):
            max += 1
            acc = re.search(r"^>.*(\d\|)", line)
        #Extracts length by finding match and stores to new variable
        elif line.startswith('Length='):
            length = line.rstrip("\n") 
        #Extracts score by finding match and stores to new variable
        elif line.startswith(' Score'):
            score = re.search(r"\bScore.*(\d )",line)

            #Writes to stdout the accession, score and length of first 10 alignments in desired format            
            sys.stdout.write("Alignment #" + str(max) + ": Accession = " + acc.group().strip(">") + "(" + length + ", " + score.group().rstrip(' ') + ")\n")
            #End function when 10 alignments read
            if max == 10:
                break
        #Skip lines that do not hold information to be extracted
        else:
            continue
        
#Read each line of file to extract query ID and length 
while my_entries:
    #Extracts query ID by finding match and stores to new variable
    k = re.search(r"^Query=(.*)", my_entries)
    #If match found move to next lines to find query length 
    if k: 
        #Stores actual query ID to new variable 
        queryid = k.group(1)
        #Move to new lines to fine query  
        my_entries = my_file.readline()
        my_entries = my_file.readline()
        #Extracts query length by finding match and stores to new variable
        l = re.search(r"^Length=(.*)", my_entries)
        #Stores actual query length to new variable 
        querylength = l.group(1)
        #Writes to stdout the actual query ID and query length in desired format   
        sys.stdout.write("Query ID: "+ queryid + "\n" + "Query Length: " + querylength + "\n")
        #Initiates function to extract information from top 10 alignments
        alignments()
    #Reads next line    
    else:
        my_entries = my_file.readline()

my_file.close() #closes file
