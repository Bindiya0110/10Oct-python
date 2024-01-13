k = input("Enter your String : ")

if len(k) < 3:
    print(k)
elif k[-3]=='ing':
    print(k + 'ly')
else:
    print(k + 'ing')