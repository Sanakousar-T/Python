"""
Combine 2 list and convert it to a dictionary as shown below
list1=['a','b','c']
list2=[1,2,3]
Expected Output:{'a': 1, 'b': 2, 'c': 3}
"""

list1=['a','b','c']
list2=[1,2,3]

#way1 : using zip fuction
dict1=dict(zip(list1,list2))
print(dict1)

#way2 : Using Comprehension 
dict2={list1[i]:list2[i] for i in range(len(list1))}
print(dict2)

#way3 : Using nested for loop
dict3={}
for key in list1:
    for value in list2:
        dict3[key]=value
        list2.remove(value)
        break
print(dict3)

#output:
"""
{'a': 1, 'b': 2, 'c': 3}
{'a': 1, 'b': 2, 'c': 3}
{'a': 1, 'b': 2, 'c': 3}

"""
