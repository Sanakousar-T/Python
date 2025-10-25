"""
OPERATORS :

--> These are library functions which are mean to perform specific task(operation).

--> operators are also called as special symbols.

--> To perform any operation we need operands and operators.

--> operands : These are the values which are passed to perform some operation.

Types of operators :

1) Arithmetic operators
2) Relational operators
3) Logical operators
4) Bitwise operators
5) Assignment operators
6) Membership operators
7) Identity operators

1) Arithmetic operators :-

--> These are the opearators which performs arithmetic opeartions

Types : 

1) Addition (+)
2) Subtraction (-) 
3) Multiplication (*)
4) Division  ---->  i)   true division (/)
                    ii)  floor division (//)
                    iii) Modulus division (%)
5) Power(**)


1) Addition (+) :-

Syntax : op1 + op2

--> It is an operator which gives sum of two or more operands in case of single 
    value data types
--> In case of Multivalue/collection datatypes, it is used to perform concatination

NOTE :-

1) While concatinating oprands must be of same datatype.
2) Addition operator will not support for set and dict.
"""
#EXAMPLE :-
55+66
121
55+1.25
56.25
55+1+2j
(56+2j)
55+True
56

'hello'+'good'
'hellogood'

[1,2,3]+['ok',3,2.56]
[1, 2, 3, 'ok', 3, 2.56]

'hi'+[1,2] --> Error

(1,2)+(1,2)
(1, 2, 1, 2)

{1,2}+{1,2} --> Error
{1:2}+{3:4} --> Error

"""
2) SUBTRACTION (-) :-

--> It is an oprator which is used to find the difference between the oprands.

Syntax : op1 - op2

--> It supports for all the single valued datatypes but in case of collection
    it supports only for set.
"""
#EXAMPLE :

10-5
5
5.25-True
4.25
1+2j-False
(1+2j)

'hi'-'hello'      ----> Error
[1,2]-[1,2]       ----> Error

{1,2,3}-{1,2}
{3}
{1,2,3}-{1,2,3,4}
set()
{1,2,3}-{4,5}
{1, 2, 3}

"""
3) MULTIPLICATION (*) :-

--> It is an oprator which is used to get the product of two or more oprands.

Syntax :   1) op1 * op2  ---->  For Single value datatypes
           2) op * n     ---->  For Collection datatypes

NOTE :-  1) In case of collection the value of n must be an integer.
         2) This operator will not support for set and dict
"""
#EXAMPLE :

5*6
30
1.25*4
5.0
1+2j*1+2j
(1+4j)
(1+2j)*(1+2j)
(-3+4j)

'ok'*3
'okokok'

[1,2]*4
[1, 2, 1, 2, 1, 2, 1, 2]

(1,2)*2
(1, 2, 1, 2)

{1,2}*3    ----> Error
{1:25}*4    ----> Error
"""
4) Division operator :

--> It is of 3 types : 1) true division (/)
                       2) floor division (//)
                       3) modulus division (%)

1) true division(/): It is a division operator which  gives us the exact
                     quotient value.

Syntax : op1 / op2

Example : 5 / 2    ----> 2.5

2) floor division(//): It is a division operator which  gives us the 
                       onlt integer part of quotient.

Syntax : op1 // op2

Example : 5 // 2   ----> 2

3) modulus divison(%): It is a division which gives us the reminder

Syntax : op1 % op2

Example : 5 % 2    ----> 1

NOTE : 

1) division operator will not support for collection.

2) floor division and modulus division will not support for complex.


5) power(**) :-

--> It is an operator which multiplies the given number for specified no. of times

Syntax : op ** n

--> both operand and n should be of individual datatype
--> power operator will not support for collection datatypes
"""
#Example : 

2**3
8
4**2
16
9**2
81
1.25**1.25
1.3217140793007052
28**1.25
64.40914574615377
