def a(b):
    b = [c for c in b if c]
    return b
b = [(),(1,2,3,4,5,6,7,8,8,9,10),()]
print(b)
print(a(b))