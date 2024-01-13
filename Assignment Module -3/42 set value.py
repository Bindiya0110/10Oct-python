k = [{'a':100},{'b':200}, {'c':300},{'a':300},{'b':200}, {'d':400}]

print("Original list is : ", k)

n = set(n for m in k for n in m.values())

print("After : ", n)