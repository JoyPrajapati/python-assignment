#Write a Python function to check whether a number is in a given range

def is_in_range(num, start, end):
    return start <= num <= end
number = int(input("Enter a number"))
print(is_in_range(number, 5, 15))