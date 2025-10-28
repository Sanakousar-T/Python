"""
write a program to print unique charecters in a string
str='test'
expected output: e,s
"""
str = 'test'
unique=[]
for char in str:
    if str.count(char)==1 and char not in unique:
        unique.append(char)
print(unique)

#outpur:
#['e', 's']
