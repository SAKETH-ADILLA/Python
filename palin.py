n=input("enter a value:")
rev=""
for s in n:
    rev=s+rev;
if(rev==n):
    print(n,"is palindrome...");
else:
    print(n,"is not palindrome...")
