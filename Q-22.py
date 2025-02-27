n=input("Enter a string : ")


if len(n) % 4==0:
    print(n[::-1])
else:
    print("SORRY! , Please enter a string with multiple of 4: ")