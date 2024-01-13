a = open("test.txt", "w")

b= ("This is python \nThis is not python")
a.writelines(b)
print(b)
a.close()