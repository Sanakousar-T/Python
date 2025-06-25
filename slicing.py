"""
SLICING :

--> It is a phenomenon of extracting part of values of a collection.

Syntax : var [ SI : EI :UP ]

where SI --> Starting Index
      EI --> Ending Index (It will be Excluded)
      UP --> Updation

--> Slicing works based on indexing and it is possible only on collection which  supports indexing 

--> If we are extracting from left to right then updation will be positive , else it will be negative

Example : 

s='mango'
s[0:3:1]
'man'
s[0:2:1]
'ma'

Simplified forms :-

s='mango'

s[-1:-6:-1]
'ognam'
len(s)
5
s[::-1]
'ognam'


s[0:5:2]
'mno'
s[::2]
'mno'

s='dark'

s[1:4:2]
'ak'
len(s)
4
s[1::2]
'ak'



Slicing on list :

L[0:3:1]
[10, 2.5, 'Rishab pant']

L[:3]
[10, 2.5, 'Rishab pant']

L[::-1]
[777, (1+2j), 'Rishab pant', 2.5, 10]

L[2][7:11]
'pant'

L=[10,2.5,[99,150,['kingkohli',18],45],'KLRAHUL']
L[2][2][0][:4]
'king'


NOTE :

1) Slicing on tuple works exactly like list
2) Slicing on set is not possible because indexing is not possible on set.



Slicing on dictionary :

NOTE:

Slicing on dictionary is not possible directly , but when the values are of 
collection datatype which supports indexing , then slicing can be applied.

Ex:01)

d={10:20,'hi':4.5,7:'good boy'}

d[7][5:8]
'boy'

d['hi'][::-1]  ------>ERROR

EX:02)

d={'name':'Qspiders','dob':2004,'branch':['rajajinagar','btm']}

d['branch'][0][6:]
'nagar'

d['dob'][:2]  ------>ERROR
"""