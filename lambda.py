x= lambda i: "EVEN" if i%2==0 else "ODD"
n = int(input("Enter the Number: "))
result = x(n)
print(f"The Number is: {result}")