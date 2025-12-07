# Simple If:

# 1. Wap to print the square of a number only if it is even.
"""
n = int(input("enter integer:"))
if n%2==0:
    print(n**2)
"""
# 2. Wap to check whether the character is vowel or not.
"""
ch = input("enter a character:")
if ch in 'AEIOUaeiou':
    print("the character is vowel")
"""
# 3. Wap to print Ascii value of a character only if it is upper case.
"""
ch = input("enter a character:")
if 'A' <= ch <= 'Z':
    print(ord(ch))
"""
# 4. Wap to print the cube of a number only if it is divisible by 9 or 6.
"""
n = int(input("enter a number"))
if n%9==0 and n%6==0:
    print(n**3)
"""
# 5. Wap to check whether the given integer is 3 Digit number.
"""
n = int(input("enter a number:"))
if n>99 and n<1000:
    print("the given integer is 3 Digit number")
"""
# 6. Wap to check whether the last digit of a given number is 5.
"""
n = int(input("enter a number:"))
if n%10==5:
    print("the last digit of a given number is 5")
"""
# 7. Wap to check whether the given data is float.
"""
data = eval(input("enter data:"))
if type(data) == float:
    print("the given data is float")
"""
# 8. Wap to check whether the data is single value data.
"""
data = eval(input("enter the data"))
if type(data) in [int, float, complex, bool]:
    print("the data is single value data")
"""
# 9. Wap to check whether the given character is digit or not.
"""
ch = eval(input("enter character:"))
if '0'<=ch<='9':
    print("the given character is digit")
"""
# 10. Wap to check whether the given integer is multiple of 3.
"""
n = int(input("enter integer:"))
if n%3==0:
    print("the given integer is multiple of 3")
"""













