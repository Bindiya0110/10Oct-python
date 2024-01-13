f = open("test.txt","r")
s=" "

for i in range(0,100):
    s=s + f.read(i)

print(s)