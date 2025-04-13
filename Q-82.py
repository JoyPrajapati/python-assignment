#Write a Python program to copy the contents of a file to another file.

with open("sample.txt", "r") as source_file, open("destination.txt", "w") as destination_file:
  for line in source_file:
    destination_file.write(line)
  print("File copied successfully.")