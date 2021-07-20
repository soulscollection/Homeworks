def lol(a, b, c=0):
    if a > b and a > c:
        return a
    elif a < b and c < b:
        return b
    elif a < c and b < c:
        return c
    else:
        return 0

t = lol(7, 7, 7)
print(t)
