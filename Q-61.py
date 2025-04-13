#Write a Python function to calculate the factorial of a number (a nonnegative integer)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result=1
        for i in range(1, n + 1):
            result *= i
        return result

factorial(5)