#Write a Python program to check multiple keys exists in a dictionary

keyy=int(input("Enter a key to check whether it exist or not->"))
d={1: 'a', 5: 'b', 6: 'c', 9: 'd', 12: 'e',13:'f',17:'g',19:'h',21:'i'}
if keyy in d:
  print(f"{keyy} Exist")
else:
  print(f"{keyy} Doesn't exist")