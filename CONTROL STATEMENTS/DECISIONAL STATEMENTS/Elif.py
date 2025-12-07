# 21. Wap to check whether the char is uppercase, lowercase, digit or special char.
"""
ch = input("enter character:")
if 'A' <= ch <= 'Z':
    print("the char is uppercase")
elif 'a' <= ch <= 'z':
    print("the char is lowercase")
elif '0' <= ch <= '9':
    print("the char is digit")
else:
    print("the char is special char")
"""
# 22. Wap to check whether the given integer is single digit or two digits or
# three digits or more than three digits.
"""
n = int(input("Enter a integer number:"))
if 0 <= n <= 9:
    print("the given integer is single digit")
elif 10 <= n <= 99:
    print("the given integer is two digit")
elif 100 <= n <= 999:
    print("the given integer is three digit")
else:
    print("the given integer more than three digits")
"""
# 23.Wap to check the given points are lying in which quadrant.
"""
x = int(input("x-axis:"))
y = int(input("y-axis"))
if x > 0 and y > 0:
    print("Quadrant 1")
elif x < 0 and y > 0:
    print("Quadrant 2")
elif x < 0 and y < 0:
    print("Quadrant 3")
elif x < 0 and y < 0:
    print("Quadrant 4")
else:
    print("on an axis")
"""
# 24. Wap to find the greatest of 3 numbers.
"""
a1 = int(input("Enter 1st number:"))
a2 = int(input("Enter 2nd number:"))
a3 = int(input("Enter 3rd number:"))
if a1 > a2 and a1 > a3:
    print("1st number is greater")
elif a2 > a1 and a2 > a3:
    print("2nd number is greater")
else:
    print("3rd number is greater")
"""
# 25. Wap to find the smallest of 3 numbers.
"""
a1 = int(input("Enter 1st number:"))
a2 = int(input("Enter 2nd number:"))
a3 = int(input("Enter 3rd number:"))
if a1 < a2 and a1 < a3:
    print("1st number is smallest")
elif a2 < a1 and a2 < a3:
    print("2nd number is smallest")
else:
    print("3rd number is smallest")
"""
# 26.Wap to check the relation between two integer numbers.
"""
n1 = int(input("Enter number 1:"))
n2 = int(input("enter number 2:"))
if n1 == n2:
    print(f'{n1} is equals to {n2}')
elif n1 > n2:
    print(f'{n1} is greater than {n2}')
elif n1 < n2:
    print(f'{n1} is lesser than {n2}')
"""
# 27. Consider a character input if it is uppercase convert it into lowercase, if it is
# lowercase convert it into uppercase, if it is digit print the reminder when  it is
# divided by 3 else if it is special character print it's ASCII value.
"""
ch = input("Enter character:")
if 'A' <= ch <= 'Z':
    print(f"{ch} is converted to lowercase:{chr(ord(ch)+32)}")
elif 'a' <= ch <= 'z':
    print(f"{ch} is converted to Uppercase:{chr(ord(ch)-32)}")
elif '0' <= ch <= '9':
    print(f"reminder of {ch} when it is divided by 3 :{int(ch)%3}")
else:
    print(f"ASCII value of {ch} is {ord(ch)}")
"""
# 28.Wap  to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the
# given number is multiple of 5 and print ‘Fizzbuzz’ if the number is multiple of
# both 3 and 5.
"""
n = int(input("enter number:"))
if n % 3 == 0 and n % 5 == 0:
    print("Fizzbuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("buzz")
"""



