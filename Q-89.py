#How Do You Handle Exceptions with Try/Except/Finally in Python? Explain with coding snippets.

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
finally:
    print("Execution completed.")