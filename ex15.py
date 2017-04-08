# imports the ability to use arguments from the command line
from sys import argv

# assigns the arguments to variables
script, filename = argv

# gets teh file and stores it in the txt variable
txt = open(filename)

# prints the filename and then prints the text
print "Here's your file %r:" % filename
print txt.read()
txt.close()

# gets a new or the same file from the user
print "Type the filename again:"
file_again = raw_input("> ")

# opens and stores the file again in a new variable
txt_again = open(file_again)

# prints out the file form the new variable 
print txt_again.read()
txt_again.close()
