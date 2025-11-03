#01) WAP to print square of given integer if it is even , else print cube of integer if it is odd 
-------------------------------------------------------------------------------------------------
num=int(input("enter integer:"))
if num%2==0:
    print(f'square of {num} is {num**2}')
else:
    print(f'cube of {num} is {num**3}')
  #output:

  #01)enter integer:2
  #square of 2 is 4
  #02)enter integer:3
  #cube of 3 is 27

#02) WAP to check whether the given data is immutable or mutable 
----------------------------------------------------------------
data=eval(input("enter data:"))
#print(type(data))
if type(data) in [list,set,dict]:
    print("the given data is mutable")
else:
    print("the given data is immutable")

#output:
#01)enter data:[1,2]
#the given data is mutable

#03) WAP to check whether the given character is special character or not 
ch=input("enter character:")
if not(ch.isupper or ch.islower or ch.isdigit):
    print("it is special character")
else:
    print("it is not special character")

#output:
#01)enter character:a
#it is not special character
#02)enter character:@
#it is not special character


#02)enter data:2.4
#the given data is immutable





