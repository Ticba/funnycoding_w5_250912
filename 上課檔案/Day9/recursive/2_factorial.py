# 階乘 
# 5 階乘 = 1 x 2 x 3 x 4 x 5 = 120
# 2 階乘 = 1 x 2 = 2

def fact(n):
    if n == 1:
        return 1
    return n + fact( n-1 )

print(fact(5))


# 想法
# 要算 n 階乘 = (n-1) 階乘 * n
# 例： 5 階乘 = 4 階乘 * 5
# 什麼時候要直接回傳？