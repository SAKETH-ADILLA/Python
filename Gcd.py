def gcd(a,b):
    while b:
        a, b= b, a%b
    return abs(a)
num1= 12
num2= 24
result = gcd(num1,num2)
print(f"The GCD of {num1} and {num2} are: ", result)