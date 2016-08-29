queries = int(input())

for q in range(queries):
    n = int(input())
    width = 2*n
    arr = []
    for i in range(width):
        row = [int(i) for i in input().strip().split()]
        arr.append(row)
    total = 0
    for i in range(n):
        for j in range(n):
            #get numbers in upper left quadrant
            number = arr[i][j]
            #check opposite in row
            if number < arr[i][width-1-j]:
                number = arr[i][width-1-j]
            #check opposite in column
            if number < arr[width-1-i][j]:
                number = arr[width-1-i][j]
            #check opposite in row and column
            if number < arr[width-1-i][width-1-j]:
                number = arr[width-1-i][width-1-j]
            total += number
    print(total)
        
