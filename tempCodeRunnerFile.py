n=input("Enter a string : ")

ch=""

for char in n:
        if char not in ch:
            count = n.count(char)
            print(f"'{char}': {count}")
            ch += char
            