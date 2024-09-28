def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
a= int(input("Enter the Number: "))
if a<=0:
    print("The Given Number is in Negative and Zero!! ")
else:
    print(f"The factorial of the given Number {a} is: ", fact(a))