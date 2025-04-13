#Write a Python program to count the number of lines in a text file.

with open("sample.txt", "r") as file:
  lines = file.readlines()
  print(f"Total number of lines: {len(lines)}")