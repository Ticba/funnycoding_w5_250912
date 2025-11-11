'''
模組: module

random 

time

os

sys

math

numpy (X)


模組在哪？ 已經跟 python 一起下載了 （或者另外安裝） pip


import 的方式
(1) import 模組名稱
    使用的時候：
    模組的名稱.模組內的函式()

    import random

    for i in range(6):
        result = random.randint(1, 6)
        print(result)

(2) import 模組名稱 as 暱稱
    使用的時候：
    暱稱.模組內的函式()

    import random as r

    for i in range(6):
        result = r.randint(1, 6)
        print(result)

(3) from 模組名稱 import 單一模組內的函式()
    使用的時候：
    單一模組內的函式()

    from random import randint

    for i in range(6):
        result = randint(1, 6)
        print(result)


遇到新模組的時候
(1) 先查搜尋引擎
  1-1 部落格
  1-2 論壇
(2) 問 AI 這個模組的基本功能？使用時機？
(3) 去官網看(python documentation)：特定模組內函式
'''



from random import randint, choice

for i in range(6):
    result = randint(1, 6)
    print(result)


L = ['剪刀', '石頭', '布']

for i in range(3):
    print(choice(L))