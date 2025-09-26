'''
在體育課的跳遠測驗中
男生與女生的成績標準可能不同
https://meo.meiho.edu.tw/p/405-1004-37824,c4795-1.php?Lang=zh-tw
'''


性別 = '女'  # 男\女
成績 = 170   

if 性別 == '女':
    if 成績 < 150:
        print('fail')
    else:
        print('pass')
else:
    if 成績 < 200:
        print('fail')
    else:
        print('pass')


# 第一個判斷 我：性別 == '男'              -> 性別 == '女'
# 第二個判斷 我：成績 >= 200 | 成績 >= 150 -> 成績 < XXX
