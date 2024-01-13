def a(b):
    if(b == b[::-1]):
        return"sring is pelindrom"
    else:
        return"sring is not pelindrom"

b = input("Enter your string : ")
print(a(b))