# 1. 順序很重要
#   地點，動物
# 紀錄順序的資料結構 ？ List 的 index 其實就代表加入的先後順序 
# 先看到的地點名稱就 append 進 List 中

# 2. 要計算數量
#   不同地點要分開算
'''
地點一 = {'mokey': 1}
地點二 = {}
地點三 = {}

# 所有的 地點 dict 打包成一個結構 

d = {"地點一": {"mokey": 1, "snail": 2}, "地點二": {"mokey": 2, "snail": 2}}
# 元素 in d.keys() 檢查

# 新增的時候方便
d["地點三"] = {}
'''

# 統整
# 第一個資料
# 存地點出現順序 (list)
# 存動物出現順序 (list)
# 存各個區域出現的動物數量 (dict, values 也都是 dict)

# 輸入
# 6
# monkey 2 tree
# snail 1 ground
# jackyliuxx 2 ground
# snail 1 tree
# monkey 1 ground
# snail 3 ground

n = int(input())
# 地點 list
地_li = []
動_li = []
地_dict = {} # 計數量

for i in range(n):
    animal, num, loc = input().split()
    num = int(num)
    # 到此已經拿到 animal, num, loc (分別

    # 檢查地點
    # 1. 沒出現過 => 新增到地點 list
    # 2. 出現過   => X
    if not (loc in 地_li):   # 元素 in iterable 物件
        地_li.append(loc)

    # 檢查動物
    # 1. 沒出現過 => 新增到動物 list
    # 2. 出現過   => X
    if not (animal in 動_li):   # 元素 in iterable 物件
        動_li.append(animal)

    # 計算數量
    # 1. 要檢查地點dict 有沒有該元素
    if not (loc in 地_dict.keys()):
        地_dict[loc] = {}   # dict 的新增
    
    # 2. 要檢查 地_dict[loc] (小的 dict) 有沒有數過 animal
    if not (animal in 地_dict[loc].keys()):
        地_dict[loc][animal] = 0  # dict 的新增
    地_dict[loc][animal] += num

# 輸出方式(照順序)
# tree : monkey 2, snail 1
# ground : monkey 1, snail 4, jackyliuxx 2
for 地名 in 地_li:
    print(地名, ':', end=' ')
    # 從 地_dict[地名] 找出數量，搭配 動_li 去取順序
    temp = []  # 拿來存所有的動物:數量

    for 動物名 in 動_li:
        # 有可能該地名沒有某種動物
        if 動物名 in 地_dict[地名]:
            temp.append(動物名 + ' ' + str(地_dict[地名][動物名]))
    
    # ['monkey 2', 'snail 1']
    
    print(', '.join(temp))
