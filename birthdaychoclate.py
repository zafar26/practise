Consider the chocolate bar as an array of squares,
s = [1,2,1,2,3,2]
d = 3
m = 2.

# Complete the birthday function below.
def birthday(s, d, m):
    counter = 0
    total = 0
    for i in range(len(s)):
        if m == 2:
            h = i 
            p = i+1
            if i+m > len(s):
                break
            total = s[h] +s[p]
        elif m > 2:
            h = i 
            p = i+(m-2)
            if i+m > len(s):
                break
            for h in range(p):
               total += s[h]
        elif m == 1:
            total = s[i]
        else:
            total = total
            
        if total == d:
            total = 0
            counter += 1
    return counter





