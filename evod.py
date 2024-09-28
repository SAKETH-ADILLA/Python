l=[21,32,43,79,88,69]
ev=[]
od=[]
len=len(l)
for i in range (len):
    if (l[i]%2==0):
        ev.append(l[i])
    else:
        od.append(l[i])
print("even list:",ev)
print("odd list:",od)