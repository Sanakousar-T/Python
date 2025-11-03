"""
ASSIGNMENT QUESTIONS ON simple if : 
01) WAP to check whether the given integer is odd number. 
02) WAP to check whether the given character is uppercase. 
03) WAP to check whether the last value of a list is mutable. 
04) WAP to consider 2 integers and check whether both are divisible by 5 
05) WAP to check whether the first and last character of string are same. 
06) WAP to check whether the given data is dictionary 
07) WAP to check whether the given data is default value.
"""

#01) WAP to check whether the given integer is odd number.
----------------------------------------------------------
num = int(input("enter integer number:"))
if num%2!=0:
    print("given integer is odd")
  # output:
  #enter integer number:3
  #given integer is odd

#02) WAP to check whether the given character is uppercase.
-----------------------------------------------------------
char=(input('enter a character:'))
if char.isupper():
    print("given character is uppercase")
    #output
    #enter a character:A
    #given character is uppercase

#03) WAP to check whether the last value of a list is mutable. 
--------------------------------------------------------------
list1=eval(input("enter the list:"))
#print(list1)
last_index=len(list1)-1
#print(type(list1[last_index]))
if type(list1[last_index]) in [list,set,dict]:
    print("the last value of a list is mutable")

    #output:
    #enter the list:[1,2,[1,2]]
    #the last value of a list is mutable

#04) WAP to consider 2 integers and check whether both are divisible by 5 
-------------------------------------------------------------------------
num1=int(input("enter 1st integer:"))
num2=int(input("enter 2nd integer:"))
if num1%5==0 and num2%5==0:
    print("Both are divisible by 5")

    #output:
    #enter 1st integer:10
    #enter 2nd integer:45
    #Both are divisible by 5

#05) WAP to check whether the first and last character of string are same. 
--------------------------------------------------------------------------
s=input("enter a string:")
if s[0]==s[-1]:
    print("the first and last character of string are same")

    #output:
    #enter a string:gadag
    #the first and last character of string are same

#06) WAP to check whether the given data is dictionary 
-------------------------------------------------------
data=eval(input("enter data:"))
if type(data) is dict:
    print("the given data is dictionary ")

    #output:
    #enter data:{1:'a',2:'b'}
    #the given data is dictionary 

#07) WAP to check whether the given data is default value.
----------------------------------------------------------
data=eval(input("enter data:"))
#print(bool(data))
if bool(data)==False:
    print("the given data is default value")

    #output:
    #enter data:set()
    #the given data is default value

#08) WAP to whether the given data is present in dictionary 
-----------------------------------------------------------
dict1={'a':1,'b':2,'c':3,'d':4,'e':5}
values=list(dict1.values())
data=eval(input("enter data:"))
#print(values)
if data in values:
    print("data is present")

    #output:
    #enter data:1
    #data is present
