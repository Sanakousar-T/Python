"""
S= 'abc@tux$yz'
Reverse string without changing the position of special character
"""
S= 'abc@tux$yz'
t=''
temp=[]
for ch in S:
  if not(ch.isupper() or ch.islower() or ch.isdigit()):
    temp.append(t[::-1])
    t=''
    temp.append(ch)
  elif ch.isupper() or ch.lower():
      t+=ch
temp.append(t[::-1])
print(''.join(temp))

# output: cba@xut$zy
    
