dict={1:'s',2:'b',3:'c',4:'d'}
n=int(input("enter n:"))
for i in dict:
    if (n==i):
        print("key exists and value is:",dict[n])
    else:
        print("key not exists")
        break