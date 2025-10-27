"""
input statement : input ()
---------------------------------

--> It is an inbuilt function which is used to receive the input from the user.

--> By default input() will store the input in string format

--> SYNTAX :- var = input ('message')

--> If we want the input in specific/required datatype , then we can go for
    1) typecasting manually 
    2) using eval()

--> Most of the time , if we are expecting the input in single value datatype
    we will go for typecasting manually.

Example :  
-------------

a=int(input('Enter the first number :'))
b=int(input('Enter the second number:'))
print(a+b)

#output :
Enter the first number :77
Enter the second number:10
87


eval()  :  It is an inbuilt function which  stores the input in same format
           in which user is providing.

Syntax : var = eval(input('message'))

--> if we are expecting the input in collection datatype then we will go for eval().

Example :
-----------
a=eval(input('enter the list :'))
b=eval(input('enter the list :'))
print(a+b)

#output :
enter the list :[1,2,3]
enter the list :[4,5]
[1,2,3,4,5]

________________________________________________________________________________________________________

print statement:
--------------------

--> It is an inbuilt function which is used to display the output.

Syntax :    print( val1,val2,val3....valn  ,  sep=' '   ,  end='\n'  )

--> It is possible to pass multiple values in print function.

--> In this function there are some default parameters those are - seperator and end.

--> sep(seperator) :- when multiple values are present by default sep will take empty space.
                      It can be modified according to requirement.

--> end :- when multiple print statements are present by default values will be printed in next line.
           It can also be modified.

EXAMPLE :

print(10,20,30 , sep='&')
print('hi','bye' , end='99')
print('bye')

#output :

10&20&30
hi bye99bye

"""

"""
#01) WAP to print square of a integer number

num=int(input('Enter a number :'))
print('The square of ',num,'is',num**2)
#print(f'The square of {num} is {num**2})

#ouput :

Enter a number :9
The square of 9 is 81


#02) WAP to reverse a string

s=input('Enter the string :')
print('Reversed string is :',s[::-1])

#output :
Enter the string :Mother
Reversed string is : rehtoM


#03) WAP to find area of rectangle

L=int(input('Enter the length :'))
B=int(input('Enter the breadth :'))
print('Area of the rectangle is :',L*B)

#output :
Enter the length :25
Enter the breadth :4
"""
Area of the rectangle is : 100
