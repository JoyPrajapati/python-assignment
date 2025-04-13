#Python program to count the number of strings where the string  length is 2 or more and the first and last character are same from a given list of strings.


words = ["level", "hello", "abc", "radar", "wow", "python", "aa", "bcb"]
count = 0
for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1
        print(word)
print("Count of matching strings:", count)
