def func():
    # 在這個區塊定義 func
    pass

# ===以下程式請勿更動===
in_s = input().split()
in_s = in_s[1:]
for i, item in enumerate(in_s):
    in_s[i] = int(item)
in_s.sort()
#執行至此 in_s 已經由小大到排好順序

ans = func(in_s) #回傳 True/False

print(in_s[0], in_s[-1], 'yes' if ans else 'no')