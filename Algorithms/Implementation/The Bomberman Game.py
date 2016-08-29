#https://www.hackerrank.com/challenges/bomber-man

def print_array(arr):
    for i in range(len(arr)):
        string = ''.join(str(c) for c in arr[i])
        print(string)

def convert_numbers(arr):
    #convert all numbers to "O"
    arr_temp = []
    for r in range(len(arr)):
        inner_list = []
        for c in range(len(arr[r])):
            if isinstance(arr[r][c],int):
                inner_list.append("O")
            else:
                inner_list.append(".")
        arr_temp.append(inner_list)
    return(arr_temp)

def tick(arr):
    #create the explosion map
    explosion_map = []
    for r in range(len(arr)):
        inner_list = []
        for c in range(len(arr[r])):
            inner_list.append(0)
        explosion_map.append(inner_list)
    #decrement the bomb timers by 1
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if isinstance(arr[r][c],int):
                arr[r][c] -= 1
            #if the bomb timer = 0
            if arr[r][c] == 0:
                #explode the bomb and its neighbors in the explosion map
                explosion_map[r][c] = 1
                if r > 0:
                    explosion_map[r-1][c] = 1
                if r < len(arr)-1:
                    explosion_map[r+1][c] = 1
                if c > 0:
                    explosion_map[r][c-1] = 1
                if c < len(arr[r])-1:
                    explosion_map[r][c+1] = 1
    #resolve the explosion map with the array
    for r in range(len(explosion_map)):
        for c in range(len(explosion_map[r])):
            if explosion_map[r][c] == 1:
                arr[r][c] = "."

def fill_array(arr):
    #fill the empty spaces in the array with new bombs of value 3
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r][c] == ".":
                arr[r][c] = 3

def copy_list(arr):
    arr_temp = []
    for r in range(len(arr)):
        inner_list = []
        for c in range(len(arr[r])):
                inner_list.append(arr[r][c])
        arr_temp.append(inner_list)
    return(arr_temp)


rows,cols,seconds = input().strip().split(' ')
rows,cols,seconds = [int(rows),int(cols),int(seconds)]

#create list from inputs
arr = []
for i in range(rows):
    arr.append(list(input()))

#convert the bombs to numbers denoting the seconds until the bomb blows up
for r in range(rows):
    for c in range(cols):
        if arr[r][c] == "O":
            arr[r][c] = 3

state_0 = copy_list(arr)
for t in range(1,6):
    tick(arr)
    if t%2 == 0:
        fill_array(arr)
    if t == 2:
        state_1 = copy_list(arr)
    if t == 3:
        state_2 = copy_list(arr)
    if t == 5:
        state_3 = copy_list(arr)


if seconds == 0 or seconds ==1:
    end_state = state_0
elif (seconds-1)%2 != 0:
    end_state = state_1
elif (seconds-1)%4 == 0:
    end_state = state_3
elif (seconds-1)%2 == 0:
    end_state = state_2

result = convert_numbers(end_state)
print_array(result)
