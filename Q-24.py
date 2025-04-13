# Write a Python function to insert a string in the middle of a string.

n=input("Enter a string : ")
insert_s=input("Enter a string : ")

middle=len(n)/2

new_str=n[:int(middle)]+insert_s+n[int(middle):]

print("new string is : ", new_str)

