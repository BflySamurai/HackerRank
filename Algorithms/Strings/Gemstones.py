#https://www.hackerrank.com/challenges/gem-stones

N = int(input())

gem_elements = []
for n in range(N):
    rock = input()
    elements = []
    if len(gem_elements) == 0: #add all elements from first rock to the list
        for e in rock:
            if not e in gem_elements:
                gem_elements.append(e)
    else:
        for e in rock: #create list of elements in this rock
            if not e in elements:
                elements.append(e)
        e = 0
        while e < len(gem_elements): #go through the elements in the gem list
            if not gem_elements[e] in rock: #if the element doesn't exist in the current rock
                gem_elements.pop(e)
            else:
                e += 1
    if len(gem_elements) == 0: #if there are no elements in common at any point
        break

print(len(gem_elements))
