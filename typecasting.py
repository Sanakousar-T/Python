"""
TYPECASTING :
--------------

It is a phenomenon of converting type of data from one type to
another type.

Syntax : dest_var = dest_type(var/val)

1)int 

Ex : a=10

b=int(a)
b
10
c=float(a)
c
10.0
d=complex(a)
d
(10+0j)
e=bool(a)
e
True
f=str(a)
f
'10'

g=list(a)   -----> Error
h=tuple(a)  -----> Error 
i=set(a)    -----> Error
j=dict(a)   -----> Error

2) float

Ex : a=2.5

int(a)
2
float(a)
2.5
complex(a)
(2.5+0j)
bool(a)
True
str(a)
'2.5'

list(a)   ----> Error
tuple(a)  ----> Error
set(a)    ----> Error
dict(a)   ----> Error


3)complex

Ex: a=2+3j

int(a)     ----> Error
float(a)   ----> Error

complex(a)
(2+3j)

bool(a)
True

str(a)
'(2+3j)'

list(a)    ----> Error
tuple(a)   ----> Error
set(a)     ----> Error
dict(a)    ----> Error

4)bool

Ex : a=True
     b=False

int(a)
1
int(b)
0
float(a)
1.0
float(b)
0.0
complex(a)
(1+0j)
complex(b)
0j
bool(a)
True
bool(b)
False
str(a)
'True'
str(b)
'False'

list(a)    ----> Error
tuple(a)   ----> Error
set(a)     ----> Error
dict(a)    ----> Error


5) string

s='mango'
a='1234'
b='4.5'

int(s)       ------>Error
int(a)
1234
int(b)        ------>Error

float(s)    ------>Error
float(a)
1234.0
float(b)
4.5

complex(s)    ------>Error
complex(a)
(1234+0j)
complex(b)
(4.5+0j)

bool(s)
True
bool('')
False

str(s)
'mango'

list(s)
['m', 'a', 'n', 'g', 'o']

tuple(s)
('m', 'a', 'n', 'g', 'o')

set(s)
{'m', 'g', 'a', 'n', 'o'}

dict(s)        ------>Error

6) list 

L=[1,2,'hi',2.5]

int(L)     ------> Error
float(L)   ------> Error
complex(L) ------> Error

bool(L)
True
str(L)
"[1, 2, 'hi', 2.5]"
list(L)
[1, 2, 'hi', 2.5]
tuple(L)
(1, 2, 'hi', 2.5)
set(L)
{1, 2, 2.5, 'hi'}

dict(L)  ------> Error

x=['ok',[1,2],(4.5,25)]
dict(x)
{'o': 'k', 1: 2, 4.5: 25}

NOTE :  CONVERSION OF TUPLE , SET INTO ALL  DATATYPES WORKS SIMILAR TO LIST .


9) dict 

d={10:20,2.35:'hi','ok':'deepavali'}

int(d)       ------> Error
float(d)     ------> Error
complex(d)   ------> Error

bool(d)
True

str(d)
"{10: 20, 2.35: 'hi', 'ok': 'deepavali'}"

list(d)
[10, 2.35, 'ok']

tuple(d)
(10, 2.35, 'ok')

set(d)
{'ok', 10, 2.35}

dict(d)
{10: 20, 2.35: 'hi', 'ok': 'deepavali'}


examples:-->

complex(7)
(7+0j)

int('1230')
1230

dict({'77'})
{'7': '7'}

dict({(7,7)})
{7: 7}

str(False)
'False'

complex(False)
0j

len(tuple({'5555'}))
1

len({'7777'})
1

len({{7,7,7,7}})  ----error
complex('False')   ----error
dict({(77)})  ----error
int(7+0j)v ----error
int('123.0')  ----error
"""
