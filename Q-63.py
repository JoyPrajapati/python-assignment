#Write a Python function to check whether a number is perfect or not.

def is_perfect():
  number=int(input("Enter a number to check whether it's perfect or not->"))
  if number < 1:
    return False
  sum_of_divisors = 0
  i = 1
  while i <= number // 2:
    if number % i == 0:
      sum_of_divisors += i
    i += 1
  return sum_of_divisors == number

is_perfect()