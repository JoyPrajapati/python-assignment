#Write a Python program to read first n lines of a file.
n = int(input("Enter the number of lines to read: "))
with open("sample.txt", "r") as file:
  for i in range(n):
    line = file.readline()
    if line:
      print(line.strip())
    else:
      break