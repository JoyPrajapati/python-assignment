# program to sum of the first n positive integers


n=int(input("Enter a number starting from 0: "))


sum=0

while n>0:
    sum=sum+n
    n=n-1
print("sum ",sum)
    

#*************************USING FOR LOOP***************************************************


n=int(input("Enter a number starting from 0: "))
if n<0:
    print("Please enter a positive number") 
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum ",sum,end=" ")
    