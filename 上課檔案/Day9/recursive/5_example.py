# 費氏數列: 
# a0 = 0, a1 = 1
# a_n = a_(n-2) + a_(n-1)   | a2 = a0 + a1  |  a3 = a1 + a2
# a2 = 1 | a3 = 2 | a4 = 3 | a5 = 5 | a6 = 8 | a7 = 13


def g(n):
    if n <= 1:
        return n
    return g(n-1) + g(n-2)

print( g(6) )