#Write a Python program to write a list to a file.

my_list = ["apple", "banana", "cherry", "date", "elderberry"]
with open("sample.txt", "w") as file:
  for item in my_list:
    file.write(item + "\n")
  print("List has been written to the file successfully.")