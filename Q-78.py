#Write a python program to find the longest words.

with open("sample.txt", "r") as file:
  words = file.read().split()
  max_length = max(len(word) for word in words)
  longest_words = [word for word in words if len(word) == max_length]
  print("Longest words in the file:", longest_words)