# 格式化

'Hi, my name is ____, I am ____ years old.'

'''
Kevin 18
alan  30
mary   7
print('Hi, my name is Kevin, I am 18 years old.')
print('Hi, my name is alan, I am 30 years old.')
print('Hi, my name is mary, I am 7 years old.')
names = ['Kevin', 'alna', 'mary']
ages = ['18', '30', '7']
print('Hi, my name is '+ names[0] +', I am '+ages[0]+' years old.')  # +   /    print(,,,,,)
print('Hi, my name is '+ names[1] +', I am '+ages[1]+' years old.')
print('Hi, my name is '+ names[2] +', I am '+ages[2]+' years old.')
'''

#format
'''
(1)%
print('Hi, my name is %s, I am %d years old, I like %s.' %(names[0], ages[0], toys[0]))
print('Hi, my name is %s, I am %d years old.' %(names[1], ages[1]))
print('Hi, my name is %s, I am %d years old.' %(names[2], ages[2]))

%s -> str
%d -> int
%f -> float

(2).format()

input().strip()   # . 意思是作用於前者

print('Hi, my name is {}, I am {} years old.'.format(names[0], ages[0]))
print('Hi, my name is {}, I am {} years old.'.format(names[1], ages[1]))
print('Hi, my name is {}, I am {} years old.'.format(names[2], ages[2]))

(3) f-string 
洞裡直接放你要的東西

f''

(4) 對齊
f-string -> {程式:格式}
{程式:5}


'''
names = ['Kevin', 'alan', 'mary']
ages = [18, 30, 7]
toys = ['dragon', 'gun', 'stick']

print(f'Hi, my name is {names[0]:5}, I am {ages[0]:03} years old.')  # 出現 {}，就會把中間的程式先執行
print(f'Hi, my name is {names[1]:5}, I am {ages[1]:03} years old.')
print(f'Hi, my name is {names[2]:5}, I am {ages[2]:03} years old.')

# 18
# 30
#  7
#  HH:MM:SS
#  晚上 11 點 59 分 7 秒 -> 23:59:07
