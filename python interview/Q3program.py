"""
Take the below 2 lists as input and print expected output
list1=['my','name']
list2=['is','john']
Expected output:my name is john
"""
list1=['my','name']
list2=['is','john']

#way1 : using + operator
list3= list1+list2
print(*list3) #The * unpacks the list — it sends each value separately to print().

# way2 : using extesnd and join function
list1.extend(list2)
print(' '.join(list1))

# output
#my name is john
#my name is john


