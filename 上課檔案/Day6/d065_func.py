def my_max():
    # 在這個區塊定義 my_max
    pass

# ===以下程式請勿更動===

items = input().split()

my_list = []
for i in range(len(items)):
    my_list.append(int(items[i]))
print(my_max(my_list))