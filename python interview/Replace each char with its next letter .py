"""
s= 'Juniper'
Replace each char with its next letter 
Expected output: 'Kvojqfs'
"""
s = 'Juniper'
result = ''
for i in range(len(s)):
    ch = ord(s[i])
    result+=str(chr(ch+1))
print(result)

# outpur: Kvojqfs
