'''
使用者輸入: 3

*
**
***

使用者輸入: 5

*
**
***
****
*****

'''

# n = int(input())
# print('*', end='')    # 1個
# print()



# print('*', end='')
# print('*', end='')   # 2個  i=2, j=
# print()


# print('*', end='')
# print('*', end='')
# print('*', end='')  # 3個
# print()
# n = 3
# for i in range(1, n+1): # 1:1, 2:2, 3:3
#     for j in range(i):
#         print('*', end='')
#     print()

# 輸出 '***'
# print('*'*3)  #    * 是運算子     str * int -> str 重複串接 int 次數

n = 3
# for i in range(1, n+1): # 1:1, 2:2, 3:3
#     #  i: 1->1, 2->2, 3-> 3
#     print('*'*i)      # 1: * 一個,   2: ** 兩個,    3: *** 三個
for i in range(1,n+1):   # 3 start, 4 stop(不包含) 
    # 迴圈只跑一次, i = 3
    print('*'*i)


# 練習題：
# 使用者輸入：
# 3   (總共幾個三角形)
# 2   (第一個幾層)
# 4   (第二個幾層)
# 5   (第三個幾層)


'''
*
**
*
**
***
****
*
**
***
****
*****
'''
x = int(input())
for j in range(x):
    n = int(input())
    for i in range(1, n+1): # 1:1, 2:2, 3:3
        print('*'*i)