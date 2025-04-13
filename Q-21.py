#program to add 'in' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is 
# less than 3, leave it unchanged. 

n=input("Enter a string : ")

if n.endswith("ing"):
    n+="ly"
    print(n)
elif len(n)>=3:
    n+="in"
    print(n)
else:
    print(n)