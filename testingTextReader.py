# Tommy Tran 2420005 
# OS Assignment 2 
# Text Reader without threads


######## TESTING SITE ############

import re # regular expression
import time  # for time package


def main():
    start = time.time()
    # Select a file to only read
    f = open("enwik9", "r")
   
    # reads and places the doc into a var 
    theFile = f.readline()
    numFile = len(f.readlines())

    # test to use a loop to read each line 
    for i in f:
        #print(f.readline())
        #print(num) #possible number of lines
        #num +=1 

        # need to add the methods of performing the conversions and then reread
        testX = re.sub("[\'\"+=*.<>\/[]|(){}:]", " ", theFile)
        wordTest = testX.split()
        print(wordTest)
        print(len(wordTest))

    # sub the line for special character test
    #x = re.sub("[\'\"+=*.<>\/[]|(){}:]", " ",theFile)  # works

    # read and priont 100 characters as a test
    #print(f.read(100))  # works
    
    # read a line
    #print(f.readline()) # works

    # split the words up into individuals
    #words = x.split()

    # testing purpose to print out the one line and print the len of the list
    #print(words)
    #print(len(words))
    
    # test print what's in words
    #print(words[1])  # this will print one word from the list 

    # test print len()
    #print(len(words[1])) #this will print the length of the char in the word (which is index 1)

    # Always close after open
    f.close()
    end = time.time()
    print(end - start)


main()      # this reads one line of text and splits them up in a list
