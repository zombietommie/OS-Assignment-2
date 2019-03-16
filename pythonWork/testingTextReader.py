# Tommy Tran 2420005 
# OS Assignment 2 
# Text Reader without threads


######## TESTING SITE ############

import re # regular expression
import time  # for time package

def fileRead():
    # Select a file to only read
    f = open("enwik9", "r")

    # test to use a loop to read each line 
    wordTest = []
    words = []
    count = []
    counter = 10000
    for i in f:
        counter -= 1
        if (counter == 0):
            break
        theFile = f.readline()
        # need to add the methods of performing the conversions and then reread
        testX = re.sub("['\"&;%+=*.<>\/\[\]\,()\|{}\:]", " ", theFile)
        wordTest += testX.split()
        #print(wordTest)
        #print(len(wordTest))
        # get and increment the list indexes
    wordIndex = 0  
    holdList = []
    lingList = []
    for k in wordTest:
        try:    
            count[words.index(k)] += 1
        except: 
            words.append(k)
            count.append(1) 
        try:    
            lingList[holdList.index(len(k))] += 1
        except: 
            holdList.append(len(k))
            lingList.append(1)
    for p in holdList:
        print("word length")
        print(p)
        print("word count son")
        print(lingList[wordIndex])
        wordIndex += 1
    # Always close after open
    print(len(wordTest))
    print(len(words))
    f.close()


def main():
    # start the timer 
    start = time.time()
    fileRead()
    end = time.time()
    print(end - start)


main()      # this reads one line of text and splits them up in a list
