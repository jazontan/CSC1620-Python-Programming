num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print (num1, end= "  ")
print (num2, end= "  ")
total = num1 - num2
while total > 0:
    print (total, end= "  ")
    num1 = num2
    num2 = total
    total = num1-num2
    
