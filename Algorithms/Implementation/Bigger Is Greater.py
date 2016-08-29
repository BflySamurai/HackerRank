#https://www.hackerrank.com/challenges/bigger-is-greater

def reverse_range(start, end, step):
    while start >= end:
        yield start
        start += step

def swap(word):
    letter = -1
    end = len(word)-1
    #Go through each letter in the word starting with the second to last
    for j in reverse_range(end-1,0,-1):
        #Find the smallest letter out of the ones beyond the target letter
        l = word[end]
        smallest_larger = []
        for k in range(j+1,end+1): #find all the letters larger than the current letter
            if word[k] > word[j]:
                smallest_larger.append(k)
        l = 0
        for i in range(len(smallest_larger)): #find the smallest of these numbers
            if smallest_larger[i] > l:
                l = smallest_larger[i]
        #See if this smallest letter can be swapped with our target lettter to make the next largest word
        if l > 0:
            letter = [j,l]
            return(letter)
    return("no answer")

n = int(input())

arr = []



for i in range(n):
    arr.append(list(input()))
    #arr.append(input())

for i in range(len(arr)):
    word = arr[i]
    #print(word)
    swap_letters = swap(word)
    if swap_letters == "no answer":
        print(swap_letters)
    else:
        #swap the desired letters
        temp = word[swap_letters[0]]
        word[swap_letters[0]] = word[swap_letters[1]]
        word[swap_letters[1]] = temp
        #arrange the letters to the right of the swap to form the smallest word
        while True:
            changed = False
            for i in range(swap_letters[0]+1,len(word)-1):
                if word[i] > word[i+1]:
                    changed = True
                    #swap the desired letters
                    temp = word[i]
                    word[i] = word[i+1]
                    word[i+1] = temp
            if changed == False:
                break
        string = ''.join(word)
        print(string)
