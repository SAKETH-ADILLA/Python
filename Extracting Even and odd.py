l = []
n = int(input("Enter the no of Element"))
for i in range(n):
    ele = int(input("Enter the Element"))
    l.append(ele)
print("List:", l)
even = []
odd = []
for i in range(len(l)):
    if(l[i]%2==0):
        even.append(l[i])
    else:
        odd.append(l[i])
print("Even Values:",even)
print("Odd values:",odd)
