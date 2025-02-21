#program to sum of three given integers. However, if two values are equal sum will be zero.

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

num=0
if a==b or a==c or b==c:
    print("Sum is : ",num,",Sorry enter unique numbers")
    
else:
    print("Sum is : ",a+b+c)
