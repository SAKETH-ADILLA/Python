N = 0
even = []
odd = []
N = int(input("Enter number of elements"))
for i in range(N):
    value = int(input("Enter a value: "))
    if( value%2 == 0):
        even.append(value)
    else:
        odd.append(value)
print("Even elemetns: ",even)
print("Odd elements",odd)
