#Python program that will return true if the two given integer values are equal or their sum or difference is 5. 

n=int(input("Enter number a : "))
o=int(input("Enter number b : "))

while n+o==5 or n-o==5:
    print("True")
    break