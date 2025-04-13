#Write a Python program to get unique values from a list

my_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 3]
unique_values = []
for item in my_list:
    if item not in unique_values:
        unique_values.append(item)
print("Unique values:", unique_values)