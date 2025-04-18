#Write python program that user to enter only odd numbers, else will raise an exception.

try:
    num = int(input("Enter an odd number: "))
    if num % 2 == 0:
        raise ValueError("Error: Only odd numbers are allowed!")
    print(f"Valid input: {num} is an odd number.")
except ValueError as e:
    print(e)