#program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 

n=input("Enter a string : ")
o=input("Enter another string: ")


new_s=o[:2]+n[2:]
new_o=n[:2]+o[2:]


res=new_s+ " " +new_o

print(res)

    
    
        
