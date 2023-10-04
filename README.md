# BLASTNparse

Write a program that will open a BLASTN (nucleotide to nucleotide search) output file, parse out 
specific information, and produce formatted output that will be written to STDOUT (i.e. Standard 
Output; the terminal window / command line).

Your program should start by opening the input file (you may hardcode the filename in this case), 
parsing and storing both the query sequence ID (from near the top of the file; look for the string 
following “Query=“) and the query length (found on the line below the query sequence), and displaying 
them both to STDOUT. 

You must use regular expressions to pull out precisely the parts of the file that you want, which is the 
definition of parsing. Hint: you will very likely need to use parentheses to put some parts of those 
expressions into temporary memory (m.group(1), etc.) for later use.

Do not have your regular expression search for hardcoded values; your program should be able to read 
another BLASTN output file and run successfully, not just this specific one.
