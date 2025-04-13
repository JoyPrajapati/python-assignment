#Write a Python program to read last n lines of a file

n = int(input("Enter the number of lines to read: "))
with open("sample.txt", "r") as file:
  lines = file.readlines()
  last_n_lines = lines[-n:]
  for line in last_n_lines:
    print(line.strip())