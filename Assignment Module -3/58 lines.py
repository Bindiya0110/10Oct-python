import random

lines = open('myfile.txt').read().splitlines()
myline =random.choice(lines)
print(myline)