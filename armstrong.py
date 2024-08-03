num = int(input("Enter a value:"))  

temp = num
rev = 0  
while(num > 0):  
    dig = num % 10  
    rev += dig **3 
    num = num // 10  
if(temp == rev):  
    print("This value is a armstrong number!")  
else:  
    print("This value is not a armstrong number!")  





 