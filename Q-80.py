#Write a Python program to count the frequency of words in a file.

with open("sample.txt", "r") as file:
  text = file.read().lower()
  words = text.split()
  word_count = Counter(words)
  for word, count in word_count.items():
        print(f"{word}: {count}")