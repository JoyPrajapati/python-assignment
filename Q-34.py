# Python function that takes two lists and returns true if they have at least ne common member.

def common_member():
  list1=list(input("Enter first list "))
  list2=list(input("Enter second list "))
  if set(list1).intersection(list2):
    return True
  else:
    return False
common_member()