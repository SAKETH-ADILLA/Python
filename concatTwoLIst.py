l1 = ["M","na","i","iron"]
l2 = ["y","me","s","man"]

l3 = list(zip(l1,l2))
print(l3)
a= []
for i in l3:
    a.append(i[0]+i[1])
print(a)