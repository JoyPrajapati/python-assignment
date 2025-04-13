#Write a Python function that checks whether a passed string is palindrome or not

def is_palindrome():
    s=input('Enter the string->')
    return s==s[::-1]
is_palindrome()