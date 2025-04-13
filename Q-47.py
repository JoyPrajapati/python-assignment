#How will you create a dictionary using tuples in python?

# List of tuples
tuples_list = [(101, 'John'), (102, 'Emma'), (103, 'Liam')]

# Dictionary comprehension
my_dict = {key: value for key, value in tuples_list}

print("Dictionary:", my_dict)