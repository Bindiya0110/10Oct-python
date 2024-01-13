k = input('Enter frist string : ')
b = input('Enter second string : ')

n = b[:2] + k[2:]
v = k[:2] + b[2:]

r = n + " " + v
print("Your string is : ", r)