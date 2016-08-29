#https://www.hackerrank.com/challenges/manasa-and-stones

test_cases = int(input())

for t in range(test_cases):
    stones = int(input())
    a = int(input())
    b = int(input())
    if b < a: #make "a" the smaller of the two
        a,b = b,a
    current_value = a * (stones-1)
    maximum = b * (stones-1)
    values = [str(current_value)]
    while True:
        if a == b:
            break
        current_value = current_value - a + b
        values.append(str(current_value))
        if current_value >= maximum:
            break

    print(" ".join(values))
