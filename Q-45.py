#Write a Python program to unzip a list of tuples into individual lists.

tuples_list = [(1, 'a', True), (2, 'b', False), (3, 'c', True)]
list1, list2, list3 = zip(*tuples_list)
print("List 1:", list(list1))
print("List 2:", list(list2))
print("List 3:", list(list3))