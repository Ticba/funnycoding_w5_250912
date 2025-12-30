# 語法 try-except
'''
try:
    # 你要執行的主要內容
    1 + input() # int + str
except TypeError:
    # 當上方區塊出現 ZeroDivisionError 就會跳來這裡
    print('hi')

print('after')
'''



while True:
    try:
        n = input()
        # 執行想要的邏輯
    except EOFError:
        print('沒了')
        break
