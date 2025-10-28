"""
Write a python program to find duplicate charecters in the below list
list1=['india','is','my','country']
Expected output: ['i','n','y']
"""
list1=['india','is','my','country']
str =''.join(list1)
print(str)
duplicate=[]
for char in  str:
    if str.count(char)>1 and char not in duplicate:
        duplicate.append(char)
print(duplicate)
