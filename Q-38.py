#Write a Python program to select an item randomly from a list.

import random

my_list = [10, 20, 30, 40, 50]
random_item = random.choice(my_list)
print(f"Randomly selected item: {random_item}")