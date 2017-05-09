#https://www.hackerrank.com/challenges/designer-pdf-viewer

height = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

h_dict = {}
for i in range(26):
    h_dict[alphabet[i]] = height[i]

w_length = len(word)
w_tallest = 0
for c in word:
    if h_dict[c] > w_tallest:
        w_tallest = h_dict[c]
    

print(w_length * w_tallest)