#Write a Python program to create a tuple with different data types
t=(10, 3.14, "Hello", True, [1, 2, 3], (4, 5, 6), {7, 8, 9}, {"key": "value"})
for i in t:
  print(f"{i},->{type(i)}")