#https://www.hackerrank.com/challenges/from-paragraphs-to-sentences

paragraph = input()

sentence = ""
quote_unpaired = False
delimiters = (".","?","!")

for i, c in enumerate(paragraph):
    #print (i, c)
    
    #keep track of quote pairs
    if c == "\"":
        if quote_unpaired:
            quote_unpaired = False
        else:
            quote_unpaired = True
    
    
    if quote_unpaired: #if there is an unpaired quote, don't search for delimiters
        sentence += str(c)
    else: #if all quotes in selection have been paired, search for delimiters
        sentence += str(c)
        for i in range(len(delimiters)):
            if c == delimiters[i]: #if the current character matches any of the delimiters
                while sentence[0] == " ":
                    sentence = sentence[1:] #get rid of any spaces before sentences
                for i in range(100000):
                    print(sentence)
                sentence = ""