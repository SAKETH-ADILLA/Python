l = [1,2,3,4,5,6,7]
print(l)
Element to Remove = 3
if rem in l:
    index = l.index(Element to Remove)
    l.pop(index)
else:
    print(" {Element to remove} not found in the list ")
print("Updated List",l)
