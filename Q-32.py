# Python program to remove duplicates from a list. 

l=[10,20,30,10,40,50]

for i in l:
    if l.count(i)>1:
        l.remove(i)
        l.sort()
        print(l)
        break 

    