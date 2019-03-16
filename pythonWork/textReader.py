# Tommy Tran 2420005 
# OS Assignment 2 
# Text Reader without threads
# textReader.py

# importing the regular expression package
import re


def main():
    # Selected a file to be read ONLY assigning it a variable 'f'
    f = open("enwik9", "r")
    
    for i in len(f.readline())


    # reads and places the doc into a var 
    theFile = f.readline()

    # sub the line for special character test
    x = re.sub("[\'\"+=*.<>\/[]|(){}:]", " ",theFile)  

    # split the words up into individuals
    words = x.split() 

    # this will print one word from the list 
    print(words[1])    
    #this will print the length of the char in the word (which is index 1)
    print(len(words[1]))

    # Always close after open
    f.close()


# Run the methods (def)s 
main()
