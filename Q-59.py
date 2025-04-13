#Write a Python program to create a dictionary from a string.
###Note: Track the count of the letters from the string.

from collections import Counter
string = "programming"
letter_count = Counter(string)
print(letter_count)