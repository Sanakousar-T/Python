# If else:

# 11. Wap to check whether the data is mutable or not.
"""
data = eval(input("enter data:"))
if type(data) in [list, dict, set]:
    print("the data is mutable")
else:
    print("the data is not mutable")
"""
# 12. Wap to check whether the given character is digit or not.
"""
ch = input("enter character:")
if '0'<=ch<='9':
    print("the given character is digit")
else:
    print("the given character is not digit")
"""
# 13. Wap to check whether the given character is special or not.
"""
ch = input("enter a character:")
if not ('A'<=ch<='Z' and 'a'<=ch<='z' and '0'<=ch<='9'):
    print("the given character is special")
else:
    print("the given character is not special")
"""
# 14. Wap to check whether a list consists of middle value or not.
"""
l = eval(input("enter list:"))
if len(l)%2 != 0:
    print("list consists of middle value")
else:
    print("list not consists of middle value")
"""
# 15. Wap to check whether the number is even or odd.
"""
n = int(input("enter the number:"))
if n%2==0:
    print("the number is even")
else:
    print("the number is odd")
"""
# 16. Wap to check whether the given data is mutable or immutable.
"""
data = eval(input("enter the data:"))
if type(data) in [list, dict, set]:
    print("the given data is mutable")
else:
    print("the given data is immutable")
"""
# 17. Wap to check whether 2 values are pointing to the same memory or not.
"""
v1 = input("enter value 1:")
v2 = input("enter value 2:")
if id(v1)==id(v2):
    print("both values are pointing to the same memory")
else:
    print("both values are not pointing to the same memory")

"""
# 18. Consider a tuple of length 2 and check whether the tuple is homogenous or not.
"""
t = eval(input("enter tuple of length 2:"))
if type(t[0])==type(t[1]):
    print("the tuple is homogenous")
else:
    print("the tuple is not homogenous")
"""
# 19. Wap to check whether the string is palindrome or not.
"""
s = input("enter a string:")
if s == s[::-1]:
    print("the string is palindrome")
else:
    print("the string is not palindrome")
"""
# 20. Wap to check whether the number is positive or negative.
"""
n = int(input("enter a number:"))
if n > 0:
    print("the number is positive")
else:
    print("the number is negative")
"""









