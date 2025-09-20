# input : and apple banana cantaloupe
# output: apple and banana and cantaloupe


x = input()
y = x.split()
z = y[0]     # z = 'and'
a = y[1:]    # 串列名稱[起始:結束] -> [起始:]
b = f" {z} ".join(a)
print(b)