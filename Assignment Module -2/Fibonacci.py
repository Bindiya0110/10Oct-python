k=int(input("Enter your Value : "))
n=0
b=1
v=0

while n<k:
    print(n)
    a=n+b
    n=b
    b=a
    v += 1