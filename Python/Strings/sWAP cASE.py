#https://www.hackerrank.com/challenges/swap-case

#get the input
myString = input()

#Go through all the letters and swap their case
for i,char in enumerate(myString):
    myString = myString[:i] + myString[i].swapcase() + myString[i+1:]

#Print the new string
print(myString)