# Write a Python program to check whether a list contains a sub list

listt=[1,2,3,4,5,6,7,8,9]
sub_listt=[5,6,7]
if set(listt).intersection(sub_listt):
  print("list 2 is sub list of list 1")
else:
  print("list 2 is not sub set of list 1")