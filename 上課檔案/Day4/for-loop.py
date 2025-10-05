# 火車上有 5 名乘客，分坐在 5 節車廂
people = ['Amber', 'Julia', 'Mike', 'Leo', 'Vivian']  # 串列

# 顯示: 火車上有乘客 ____

# print('火車上有乘客', people[0])
# print('火車上有乘客', people[1])
# print('火車上有乘客', people[2])
# print('火車上有乘客', people[3])
# print('火車上有乘客', people[4])


# (1) index 索引
'''
點名單 -> 上面有車廂編號


for i in range(5):
    print('火車上有乘客', people[i])
'''


# (2) item 項目
'''
點名單空白 -> 問乘客名字並寫上

for person in people:
    print('火車上有乘客', person)   # person 每次迭代一個項目 item
'''




# 適合用索引的例子 -> 前三節車廂打折
# 顯示：火車上有乘客 ____(，有打折。)
# for i in range(5):
#     if i < 3:
#         print('火車上有乘客', people[i], '有打折') # 有打折
#     else:
#         print('火車上有乘客', people[i]) # 沒打折

# 分支
# 1. 判斷 i 他是 0~2 的要打折
# 2. 判斷 i 他是 3 以上不打折












# 適合用項目的例子 -> 名字少於 4 個字母的打折
# 顯示：火車上有乘客 ____(，有打折。)

# len(str) -> 內容的長度/大小
# 長度 = len('apple')
# print(長度)

for person in people:
    if len(person) < 4:
        print('火車上有乘客', person, '有打折')
    else:
        print('火車上有乘客', person)

# 分支
# 1. len() < 4  有打折
# 2. len() >= 4 不打折

















# 第一題：車長幫車廂編號前 2 個的車廂乘客打折

# 第二題：車長幫名字長度為 4 以上的乘客打折












# for loop 搭配 zip
'''
'Hi, my name is ____, I am ____ years old.'


print(f'Hi, my name is {names[0]:5}, I am {ages[0]:03} years old.')
print(f'Hi, my name is {names[1]:5}, I am {ages[1]:03} years old.')
print(f'Hi, my name is {names[2]:5}, I am {ages[2]:03} years old.')
'''
names = ['Kevin', 'alan', 'mary']
ages = [18, 30, 7]

# for name in names:
#     print(name)

# for age in ages:
#     print(age)



for name, age  in zip(names, ages):   # [['Kevin', 18], ['alan', 30], ['mary', 7]]
    print(f'Hi, my name is {name:5}, I am {age:03} years old.')




people = ['Amber', 'Julia', 'Mike', 'Leo', 'Vivian']
#  乘客的要求：讓票
#  'Amber' -> 'Lisa'


people[0] = 'Lisa' # 換串列內容的方法

# 'Amber' -> 'Amber V'
# 'Julia' -> 'Julia V'
# 'Mike'  -> 'Mike V'
# 'Leo'   -> 'Leo V'
# 'Vivian'-> 'Vivian V'

# people[0] = people[0] + ' V'
# people[1] = people[1] + ' V'
# people[2] = people[2] + ' V'
# people[3] = people[3] + ' V'
# people[4] = people[4] + ' V'


# 索引值更改 item
# for i in range(5):
#     people[i] = people[i] + ' V'   # people[i] += ' V'



# item 直接更改
# 電腦裡  -> 
# 1. people = ['Amber', 'Julia', 'Mike', 'Leo', 'Vivian']
# 2. person = 'Mike V'

# for person in people:     # person 他其實也是一個變數，他都會有自己的空間
#     person = person + ' V'  #person 變成 'Amber' 


# enumerate()   ->  同時取得索引值 & item

for i, person  in enumerate(people):
    people[i] = person

# print(people)   # 輸出整個串列


