#Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

d={1: 'a', 5: 'b', 6: 'c', 9: 'd', 12: 'e',13:'f',17:'g',19:'h',21:'i'}
for key,value in d.items():
  if 1<= key <=15:
    print(f"{key} : {value}")