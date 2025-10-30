#01)WAP to check whether a candidate is eligibal to vote 
---------------------------------------------------------
age=int(input("enter the age:"))
if age>=18:
    print("candidate is eligibal to vote")
print("varified")
#output:
"""
enter the age:12
varified
--
enter the age:18
candidate is eligibal to vote
varified
--
enter the age:58
candidate is eligibal to vote
varified
"""

#02)WAP to check whether a given string has exactly 5 charecter
----------------------------------------------------------------
s=input('enter a string:')
if len(s)==5:
    print("entered string hsas 5 charecter")
#output:
#enter a string:hello
#entered string hsas 5 charecter

#03)WAP to check given integer is even
---------------------------------------
num=int(input("enter number:"))
if num%2==0:
    print("the given number is even")
#output:
#enter number:24
#the given number is even

#04)WAP to check whether the given integer is multiple of 3 and divisible by 5
--------------------------------------------------------------------------------
num=int(input("enter integer number:"))
if num%3==0 and num%5==0:
    print("the given integer is multiple of 3 and divisible by 5")
#output:
#enter integer number:15
#the given integer is multiple of 3 and divisible by 5

#05) WAP to check whether a given integer is two digit
-------------------------------------------------------
num=int(input("enter integer:"))
if num>=10 and num<=99:
    print("the given integer is two digit")
#output:
#enter integer:54
#the given integer is two digit

#06) WAP to check whether the given string is ending with 'a'
---------------------------------------------------------------
s=input('enter string:')
if s[-1]=='a':
    print("the string is ending with 'a'")
#output
#enter string:sana
#the string is ending with 'a'

#07) WAP to check whether given charecter is lowercase alphabet
----------------------------------------------------------------
ch=input("enter a charecter:")
if 'a'<=ch<='z':
    print("the given charecter is lowercase alphabet")
#output:
#enter a charecter:k
#the given charecter is lowercase alphabet

#08) WAP to check given charecter is vowel
--------------------------------------------
ch=input("enter a charecter:")
if ch in 'AEIOUaeiou':
    print("the given charecter is vowel")
#output:
#enter a charecter:i
#the given charecter is vowel

#09) WAP to check given data if float
-------------------------------------
data=eval(input("eneter data:"))
if type(data)==float:
    print('the given data is float')
#output:
#eneter data:99.9
#the given data is float

#10) WAP to print sum of to integers only if 2nd integer is greater than 1st
-----------------------------------------------------------------------------
a=int(input("enter 1st integer:"))
b=int(input("enter 2nd integer:"))
if b>a:
    print(f'sum of integers:{a+b}')
#output:
#enter 1st integer:2
#enter 2nd integer:4
#sum of integers:6

#11) WAP to check whether the given string is starting with digit and ending with uppercase alphabet
----------------------------------------------------------------------------------------------------
s=input("enter string:")
if '0'<=s[0]<='9'and s[-1].isupper():
    print("the given string is starting with digit and ending with uppercase alphabet")
#outpur:
#enter string:4K
#the given string is starting with digit and ending with uppercase alphabet






