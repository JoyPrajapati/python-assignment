#Write a Python program to read a file line by line and store it into a list

with open("sample.txt", "r") as file:
  lines = file.readlines()
  print("Lines from the file:")
  for line in lines:
    print(line.strip())

print('\nType is ')
type(lines)