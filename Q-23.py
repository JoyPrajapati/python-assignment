n=input("Enter a string : ")

if len(n)<2:
    print("enter a string having length > 2 ")
else:
    new_str=n[:2]+n[:-3:-1]
    print(new_str)