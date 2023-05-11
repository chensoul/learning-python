# Python是动态类型的语言，无须声明变量类型，直接对变量赋值即可使用
author = 'world'
print('Hello, {}!'.format(author))

# 可以一行定义多个变量
author, reader = 'hello', 'world'
# 交换变量的值
author, reader = reader, author
print(author, reader)

# 变量解包
usernames = ['hello', 'world']
# 注意：左侧变量的个数必须和待展开的列表长度相等，否则会报错
author, reader = usernames
print(author, reader)

# 变量解包：支持嵌套
attrs = [1, ['xiao_ming', 100]]
user_id, (username, score) = attrs
print(user_id, username, score)

# 变量解包：动态解包
data = ['xiao_ming', 'apple', 'orange', 'banana', 100]
username, *fruits, score = data
print(username, fruits, score)

for username, score in [('xiao_ming', 100), ('zhang_san', 60)]:
    print(username)

# 单下划线变量名：
# 1、作为一个临时变量
# 忽略展开时的第二个变量
author, _ = usernames
print(author, username)
# 忽略第一个和最后一个变量之间的所有变量
username, *_, score = data
print(author, score)

# 2、作为循环计数器
# 在循环中，如果你不需要使用计数器的值，可以将计数器命名为下划线_，以表示它是一个临时变量
for _ in range(10):
    pass

# 3、作为一个占位符
# 默认保存我们输入的上个表达式的返回值
'foo'.upper()
print(_)