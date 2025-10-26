"""
04) BITWISE OPERATORS :-
-----------------------------
--> It is an opearator which is used to perform bitwise operations.

--> It can be applied only on integers.

--> It is of 6 types :  1) Bitwise and ( & )
                        2) Bitwise or  ( | )
                        3) Bitwise xor ( ^ )
                        4) Bitwise not ( ~ )
                        5) Bitwise leftshift  ( << )
                        6) Bitwise rightshift ( >> )

1) Bitwise and ( & ) :- 
----------------------
--> It is an operator which will convert the number into binary, then it will
    perform bit by bit 'and' operation.

Syntax : op1 and op2
'''''''
truth table :-          
                         op1      op2      result

                          0        0         0
                          0        1         0
                          1        0         0
                          1        1         1
EXAMPLE:

10 & 20
0
15 & 34
2
14 & 6
6
22.5 & 5      ----->  ERROR



2) Bitwise or (|)

--> It is an operator which converts the number into binary and performs
    bit by bit 'or' operation.

Syntax :  op1  |  op2

truth table :-          
                         op1      op2      result

                          0        0         0
                          0        1         1
                          1        0         1
                          1        1         1
Example : 

22 | 2
22
10 | 7
15
150 | 33
183
33 | 12
45


3) Bitwise xor (^)

--> It is an operator which will convert the number into binary and performs 
    bit by bit 'xor' operation.
=
Syntax : op1  ^  op2

truth table :-          
                         op1      op2      result

                          0        0         0
                          0        1         1
                          1        0         1
                          1        1         0

Example :

10 ^ 7
13
33 ^ 4
37
21 ^ 2
23
17 ^ 18
3

4) Bitwise not (~) 

--> It is an oprator which is used to invert

Syntax :   ~ op

--> It works on:    -(op+1)

Example :

~17
-18
~-5
4
~1
-2
~-7
6

5) Bitwise leftshift ( << )

--> It is an oprator which converts the number into binary and it shifts the binary 
    towards left for specified number of times.

Syntax : op  << n

Example:
10 << 2
40
5<<1
10
3<<8
768

6) Bitwise rightshift ( >> )

--> It is an oprator which converts the number into binary and it shifts the binary 
    towards right for specified number of times.

Syntax : op >> n

Example:
12 >> 2
3
10 >> 4
0
7 >> 1
"""
3
