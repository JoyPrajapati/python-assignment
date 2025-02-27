#program to add 'in' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged. 

n=input("Enter a string : ")

if len(n)>=3:
    n+="in"
    print(n)
elif n=="ing":
    n+="ly"
    print(n)
else:
    print(n)