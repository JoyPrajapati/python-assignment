# program that swap two number with temp variable 
#and without temp variable


#without temp variable
n= int(input("Enter a number a number :"))
o= int(input("Enter a another number  :"))

n,o=o,n


print("numbers are",n)
print("another number is ",o)


#with temp var

n= int(input("Enter a number a number :"))
o= int(input("Enter a another number  :"))

temp=n
n=o
o=temp

print("numbers are",n)
print("another number is ",o)
