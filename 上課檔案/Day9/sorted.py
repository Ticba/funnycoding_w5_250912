# sorted() 的用法

a = [1, 2, 3]   # 排好順序的資料要找最大的兩個，就取末兩個元素
[100,90,80] # 1. 先排好（由小到大） 2. 取末兩個元素


a[-1], a[-2]    # 取末兩個元素


'''
排序
1. 自己手刻演算法


2. 已經有 function 支援你排序，要如何使用
排序好的序列 = sorted(未排序的序列)   序列使用 list



'''


# print(sorted([100,90,80]))

# 練習題：給你一堆數字（中間以空格隔開），請你輸出由小到大的結果
# 

# 範例輸入：1 2 3
# 範例輸出：1 2 3

# 範例輸入：100 90 80
# 範例輸出：80 90 100
'''
input_map = map(int, input().split())
input_list = list(input_map)

# print(sorted(input_list))           # 不會更動到 input_list
sorted_list = sorted(input_list)
result_list = list(map(str, sorted_list))

'''
# "膠水".join(list_of_string)
'''
print(" ".join(result_list))
'''



# 1. 想要照小時排大小
# sorted(b, key= 函式名稱 )  | 函式輸入是 list 裡面的元素，例 (17, 50) 要回傳的是一個數字

'''
def choose_hour(my_tuple):
    return my_tuple[0]


print(sorted(b, key=choose_hour))
'''

# 2. 想要照分鐘數排大小
'''
def choose_hour(my_tuple):
    return my_tuple[1]


print(sorted(b, key=choose_hour))
'''


# 3. 兩個都考慮 -> 照時間先後
b = [(17, 50), (17, 43), (18, 50), (18, 43)]
        #2        1          4        3

def choose_hour(my_tuple):
    # 分鐘數 + 小時數 * 60
    return my_tuple[1] + my_tuple[0] * 60


print(sorted(b, key=choose_hour))
