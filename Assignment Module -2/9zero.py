k=int(input("Enter  first Value : "))
b=int(input("Enter  second Value : "))
n=int(input("Enter third Value : "))

if k==b or b==n or n==k:
    print(" Answer is Zero")
else:
    print(f"Answer is {k+b+n}")