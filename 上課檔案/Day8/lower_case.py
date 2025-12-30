# 1. String method lower case to upper case
# 2. ASCII CODE Table 

# c = 'a'

# if ord(c) >= 97:
#     c = chr(ord(c) - 32)

# print(c)

def to_Uppercase(c):
    if ord(c) >= 97:
        c = chr(ord(c) - 32)
    return c

print(to_Uppercase('a'))  # A
print(to_Uppercase('A'))  # A

s = 'AbcDEf'
s_new = ''
for c in s:
    s_new = s_new + to_Uppercase(c)