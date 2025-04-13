#Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}

ascending_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending Order:", ascending_dict)
descending_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending Order:", descending_dict)