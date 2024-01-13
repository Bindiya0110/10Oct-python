a = (1,2,2,3,4,5,6,7,8,8,9,10)

print(a)

for i in a:
    if a.count(i)>1:
        print("Repeated",i)