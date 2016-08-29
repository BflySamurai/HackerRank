#https://www.hackerrank.com/challenges/matrix-rotation-algo

def shift(arr, n):
    a = n % len(arr)
    return arr[-a:] + arr[:-a]


#Inputs
rows,columns,rotations = input().strip().split()
rows,columns,rotations = [int(rows),int(columns),int(rotations)]


#Create array from inputs
arr_rows = []
for i in range(rows):
    arr_columns = [int(n) for n in input().strip().split()]
    arr_rows.append(arr_columns)


#Convert matrix into lines that can be rotated
arr_lines = []
width = columns
height = rows
while True:
    arr_line =[]

    width = len(arr_rows[0])
    height = len(arr_rows)

    #first row
    for i in arr_rows[0]:
        arr_line.append(i)
    arr_rows.pop(0)

    #last column
    for i in arr_rows:
        arr_line.append(i[-1])
        i.pop(-1)

    #last row
    for i in range(1, len(arr_rows[-1])+1):
        arr_line.append(arr_rows[-1][-i])
    arr_rows.pop(-1)

    #first column
    row_count = len(arr_rows)
    for i in range(1, row_count+1):
        arr_line.append(arr_rows[row_count-i][0])
        arr_rows[row_count-i].pop(0)
    arr_lines.insert(0, arr_line)

    #Break conditions
    if len(arr_rows) > 0:
        if len(arr_rows[0]) == 0:
            break
    else:
        break


#Rotate lines
arr_rotated_lines = []
for l in arr_lines:
    line_rotations = rotations%len(l)
    arr_new_line = shift(l,-line_rotations) #rotate anti-clockwise
    arr_rotated_lines.append(arr_new_line)


#Put lines back into matrix format
rotated_matrix = []

for l in arr_rotated_lines:
    rotated_matrix.insert(0,l[:width])
    l = l[width:]
    for h in range(1,height-1):
        try:
            f = rotated_matrix[h]
        except: #If this array doesn't exist, create it
            rotated_matrix.append([])
        rotated_matrix[h].insert(0,l[-1])
        l.pop(-1)
        rotated_matrix[h].append(l[0])
        l.pop(0)
    reverse_line = []
    for w in range(width):
        reverse_line.append(l[-1])
        l.pop(-1)
    rotated_matrix.append(reverse_line)
    l = l[width:]
    width += 2
    height += 2

#print the rotated matrix
for i in rotated_matrix:
    print(*i)
