#import module
from sys import argv
#state user inputs from command line
script, filename = argv
#variable to store the file
txt = open(filename)
#Print the name of the file with text
print "Here is your file %r: " % filename
#print the text from file
print txt.read()
#repeat with user input of text file
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)

print txt_again.read()
