k = []
n = int(input("Enter number of the elements : "))
for i in range(0,n):
    b=input('Enter the Elements : ' + str (i+1) )
    k.append(b)

v=len(k[0])
r=k[0]
for j in k:
    if(len(j)>v):
        v=len(j)
        r=j
print("Longest word is : ", r)