# 字典(dict) 語法
'''
dict名稱 = {}  #空字典

dict名稱 = {'A': 65, 'B':66, 'C':67}
'''

# key(身分證):value(值)

D = {
    'A':65,
    'B':66,
    'C':67
}  # 重複定義 A 的 value ，後面的會覆蓋掉前面的

print(D)

print(D['A']) # 65
print(D['B'])

# student_score = [80, 70, 100]
# student_name = ['Ticba', 'Leo', 'Amy']

student_score = {'Ticba': 80, 'Leo':70, 'Amy':100}
student_score['Ticba'] # 存取值
student_score['Ticba'] = 90 # 設定
student_score['David'] = 60 # 新增
del student_score['Ticba']  # 移除



# print(student_score)


# 搭配 for

for student in student_score:
    # student: 所有的 key
    print(student, '--->', student_score[student])

# .items() 
# .keys()
# .values()

for student, score in student_score.items():
    print(student, '--->', score)

for score in student_score.values():
    print(score)