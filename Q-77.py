#Write a Python program to read a file line by line store it into a variable.

content = ""
with open("sample.txt", "r") as file:
  for line in file:
    content += line
  print("Content of the file:")
  print(content)

type(content)