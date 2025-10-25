"""
02) RELATIONAL OPERATORS / COMPARISION OPERATORS / BOOLEAN OPERATORS

--> It is an operator which is used to compare between two or more oprands

--> This operator will give results in the form of true or false.

Types :-   1) Relational equal to (==) 
           2) Relational not equal to (!=)
           3) Relational greater than (>)
           4) Relational lesser than (<)
           5) Relational greater than or equal (>=)
           6) Relational lesser than or equal (<=)

1) Relational equal to (==) :-
---------------------------------

--> It is an operator which gives result as true, only if all the oprands are exactly same.

Syntax : op1 == op2

Example : 

9==9
True
1.23==7
False
'10'==10
False
'hi'=='hi'
True


2) Relational not equal to (!=) :-
-------------------------------

--> It is an operator which gives result as true, only if all the oprands are not same.

Syntax : op1 != op2

Example :

7!=18
True
1.25!=1.25
False
'hello'!='hi'
True
[1,2,3]!=1.25
True


3) Relational greater than (>) :-
---------------------------------

--> It is an operator which gives result as true, only if first operand is greater than second operand.

Syntax : op1 > op2

ASCCI VALUES :------>
for A to Z the range is 65 to 90              for a to z the range is 97 to 122

   A  ---- > 65                                     a  ---- > 97
   B  ---- > 66                                     b  ---- > 98
   C  ---- > 67                                     c  ---- > 99
   .                                                .
   .                                                .
   .                                                .
   Z  ---- > 90                                     z  ---- > 122

ord() :---> It is an inbuilt function which gives us Ascci value of specific character.
Syntax : ord(char)

example: 1)  ord('c')     2) ord('X')
             99              88

chr() :---> It is an inbuilt function which gives us character present at specified Ascci value.

Syntax : chr(ascci_value)

example : 1) chr(100)     2) chr(65)
             'd'              'A'
NOTE :---->

1)
2)
3)
4)
5)
6)

Example :
10>5
True
2.5>4
False
1+2j>2+2j  ----> Error

25>True
True

'hi'>[1,2,3] ----> Error

{1:2}>{25:14} ----> Error

'A'>'a'
False
'hi'>'ok'
False
'abc'>'abz'
False
'abc'>'abc'
False
'abcdef'>'abc'
True
'aBcdef'>'abc'
False


[10,20,30]>[88,99]
False
[10,20,30]>[8.8,99]
True
[10,20,30]>[10,9.9]
True
[10,20,30]>[10,20,'ab']   ----> Error

{1,2,3,4}>{1,2,3}
True
{1,2,3}>{1,2,3,4}
False
{1,2,3}>{1,2,3}
False
{1,2,3}>{4,5,6}
False 


4) Relational lesser than (<) :-
---------------------------------------

--> It is an operator which gives result as true if 1st operand is lesser than 2nd operand.

Syntax : op1 < op2

NOTE :

All the 6 note points are similar as relational greater than except 6th point

6) In set we will get result as true only if 1st oprand is subset of 2nd operand.

EXAMPLE :

{1,2,3}<{4,5,3}
False
{7,8,9,5}<{9,8,5,7,1,2}
True
{1,2}<{3,4}
False
{1,2}<{1,2}
False
{1,2,3}<{1,2}
False

[10,5]<[10,5,0.1]
True
'bZ'<'bz'
True
ord('Z')
90
ord('z')
122


05) Relational greater than or equal (>=) :-
----------------------------------------------

--> It is an operator which gives result as true only if 1st oprand is greater than 2nd or both are exactly same.

Syntax : op1 >= op2

NOTE :

All the 6 note points are similar as relational greater than except 4th and 6th point

4) If we both operands are exactly same,then it gives us result as true.
6) In set we will get result as true only if 2nd oprand is subset of 1st operand or both are same.

EXAMPLES:

1.25>=1
True
5>=55
False
55>=55
True
'hello'>='hellp'
False

06) Relational lesser than or equal (<=) :-
----------------------------------------

--> It is an operator which gives result as true only if 1st oprand is lesser than 2nd or both are exactly same.

Syntax : op1 < op2

NOTE : All the 6 note points are similar as relational greater than except 4th point and 6th point

4) If we both operands are exactly same,then it gives us result as true.
6) In set we will get result as true only if 1st oprand is subset of 2nd operand.

EXAMPLES:

10<=5
False
1.25<=1.251
True
'hi'<='hi'
True
5<=5
True"""
