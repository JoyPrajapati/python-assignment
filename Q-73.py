# Write a Python program to append text to a file and display the text.

with open("sample.txt", "a") as file:
    file.write("\nThis text is appended to the file.")

# Read and display the content of the file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)