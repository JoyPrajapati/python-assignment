#Write a Python program to find the highest 3 values in a dictionary.

d={1: 'a', 35: 'b', 6: 'c', 18: 'd', 12: 'e',13:'f',17:'g',19:'h',21:'i'}
t=sorted(d,reverse=True)
print("The highest 3 values from dictionary are")
for i in t[:3]:
  print(f"{i} : '{d[i]}'")