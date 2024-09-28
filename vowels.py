a=input("enter a string:")
COUNT=0
for i in a:
    if (i in {'a','e','i','o','u','A','E','I','O','U'}):
        COUNT=COUNT+1
print(COUNT)
