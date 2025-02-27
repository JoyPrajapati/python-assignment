#program to count the number of characters (character frequency) in a string

n=input("Enter a string : ")
ch=0
for i in n:
    if i.isalpha():
        ch=ch+1
print("characters in str is : ",ch)
for i in n:
    frequency=n.count(i)
    print(str(i) + ":" , frequency, end=", ")