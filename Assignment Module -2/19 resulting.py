k = input("Enter the  string : ")

count = k.count(k)
if 'poor' in k:
    print(k.replace("poor", "good"))
elif 'not' in k:
    print(k.replace("not", "good"))
else:
    print(k)
