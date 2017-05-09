#https://www.hackerrank.com/challenges/happy-ladybugs


Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    
    # Count the number of instances of each character
    chars = {}
    for c in b:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    
    
    answer = "YES"
    
    if "_" in chars: # If there's at least one underscore, all we needed is 2+ of each char that appears
        for key in chars:
            if key != "_":
                if chars[key] < 2:
                    answer = "NO"
                    break
    else: # If there's no underscore, we need to check to see if the conditions are met (since we can't move anything)
        # Check the ends
        if len(b) < 2:
            answer = "NO"
        elif b[0] != b[1]:
            answer = "NO"
        elif b[-1] != b[-2]:
            answer = "NO"
        else: # Check the middle
            for i in range(1, len(b)-1):
                c = b[i]
                c_prev = b[i-1]
                c_next = b[i+1]
                if (c != c_prev) and (c != c_next): # If it doesn't have any similar neighbors
                    answer = "NO"
                    break
    
    print(answer)
