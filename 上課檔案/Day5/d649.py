'''
3
5
0
'''

'''
__+
_++
+++

____+
___++
__+++
_++++
+++++
'''


while True:
    a = int(input())
    if a != 0:
        for i in range(1, a + 1):
            print("_" * (a - i) + "+" * i)
        continue
    else:
        break

# 3 5 0
a = int(input())
while a != 0:
    for i in range(1, a + 1):
        print("_" * (a - i) + "+" * i)

    a = int(input())

while True:
    a = int(input())
    if a != 0:
        for i in range(1, a + 1):
            print("_" * (a - i) + "+" * i)
    else:
        break