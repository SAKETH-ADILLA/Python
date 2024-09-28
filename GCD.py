def gcd(a,b):
    if b==0:
        return a
    else:
         return gcd(b, a%b)
num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
result = gcd(num1,num2)
print(f"The GCD of two Numbers {num1, num2} is: ", gcd(num1,num2))