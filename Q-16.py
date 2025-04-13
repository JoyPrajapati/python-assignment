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

#****************************OR*******************************

n=input("Enter a string : ")

ch=""

for char in n:
        if char not in ch:
            count = n.count(char)
            print(f"'{char}': {count}")
            ch += char
            