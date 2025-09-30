'''
sum and product of two numbers
'''

num1 = int(input("Please insert val1: "))
num2 = int(input("Please insert val2: "))

#num1 = num1 + 2
# Compute the sum
sum = num1 + num2

print("The sum of ", num1, "+", num2, "is ", sum)

if (num1 > num2):
    print("num1 > num2")
else:
    print("num1 < num2")
    
    
if (num1 > num2):
    print("num1 > num2")
elif (num1 < (num2 - 2)):
    print("num1 < num2 - 2")
else:
    print("num1 > num2 - 2")
