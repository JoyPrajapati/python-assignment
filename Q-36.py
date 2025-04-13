# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_elements():
  my_list = [1, 2, 2, 3, 4, 4, 5,6,7,8,8,9,3]
  unique_list = []
  for item in my_list:
      if item not in unique_list:
          unique_list.append(item)
  print(f"The unique list from excisting list is {unique_list}")

unique_elements()