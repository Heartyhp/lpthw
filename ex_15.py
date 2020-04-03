#importing argv module from sys library
from sys import argv

#Unpacking command line arguments
script, filename = argv

#OPening file and stroing in txt. 
txt = open(filename,closefd = True)

#Printing the file name using formatter
print(f"Here's your file {filename}")
#Reading the text from file opened recently and stored in txt.
print(txt.read())
txt.close()

print("type the file name again:")
#Asking user to enter file name 
file_again = input("> ")

#Opening file 
txt_again = open(file_again)

#Reading file Contents
print(txt_again.read())

txt_again.close()
