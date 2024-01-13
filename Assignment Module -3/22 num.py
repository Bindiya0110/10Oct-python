a = (1,2,3,4,5,6,7,8,9,10)

b = input("Enter an element to find : ")


b = int(b)

if b in a:
    print(f"{b} is in the tuple")
else:
    print(f"{b} is not in the tuple")