#!/usr/bin/env python
# coding=utf-8


str1 = 'Hello, world!'
str2 = "Hello, Python!"
str3 = """This is a long string that
spans multiple lines."""

str4 = str1 + ' ' + str2
# str4 = 'Hello, world! Hello, Python!'

ch = str1[0]  # ch = 'H'
substr = str2[7:13]  # substr = 'Python'

length = len(str3)  # length = 45

pos1 = str1.find('world')  # pos1 = 7
pos2 = str2.index('Python')  # pos2 = 7

new_str = str1.replace('world', 'Python')  # new_str = 'Hello, Python!'

words = str3.split()  # words = ['This', 'is', 'a', 'long', 'string', 'that', 'spans', 'multiple', 'lines.']

new_str = '-'.join(words)  # new_str = 'This-is-a-long-string-that-spans-multiple-lines.'

flag1 = 'world' in str1         # flag1 = True
flag2 = 'Python' not in str2    # flag2 = False

flag3 = str1.startswith('Hello')  # flag3 = True
flag4 = str2.endswith('!')        # flag4 = True

upper_str = str1.upper()  # upper_str = 'HELLO, WORLD!'
lower_str = str2.lower()  # lower_str = 'hello, python!'

str5 = '  Hello, Python!  '
new_str1 = str5.strip()  # new_str1 = 'Hello, Python!'
new_str2 = str5.lstrip()  # new_str2 = 'Hello, Python!  '
new_str3 = str5.rstrip()  # new_str3 = '  Hello, Python!'

num1 = int('123')       # num1 = 123
num2 = float('3.14')    # num2 = 3.14
num3 = complex('1+2j')  # num3 = (1+2j)

str6 = '123456'
flag5 = str6.isnumeric()  # flag5 = True

str7 = 'HelloWorld'
flag6 = str7.isalpha()  # flag6 = True

str8 = 'Hello123'
flag7 = str8.isalnum()  # flag7 = True

str9 = 'Hello, Python!'
count = str9.count('o')  # count = 2

str10 = 'Hello'
new_str4 = str10.ljust(10)  # new_str4 = 'Hello     '
new_str5 = str10.rjust(10)  # new_str5 = '     Hello'
new_str6 = str10.center(10) # new_str6 = '  Hello   '

str11 = 'Hello, Python!'
table = str.maketrans('lo', '12')
new_str7 = str11.translate(table)  # new_str7 = 'He22, Pyth2n!'

str12 = 'Hello'
new_str8 = str12.lstrip('H')  # new_str8 = 'ello'
new_str9 = str12.rstrip('o')  # new_str9 = 'Hell'

name = 'John'
age = 25
greeting = f'My name is {name}, and I am {age} years old.'
# greeting = 'My name is John, and I am 25 years old.'

pi = 3.141592653589793
print('pi = {:.2f}'.format(pi))  # 输出 'pi = 3.14'

import re

str13 = 'Hello, world!'
pattern = r'w\w+'
match = re.search(pattern, str13)
if match:
    print(match.group())  # 输出 'world'

str14 = '你好，世界！'
utf8_bytes = str14.encode('utf-8')
gb2312_bytes = str14.encode('gb2312')
utf8_str = utf8_bytes.decode('utf-8')
gb2312_str = gb2312_bytes.decode('gb2312')

str_list = ['world', 'hello', 'Python', 'java']
str_list.sort()
print(str_list)   # 输出 ['Python', 'hello', 'java', 'world']

# 对列表进行降序排序
str_list.sort(reverse=True)
print(str_list)   # 输出 ['world', 'java', 'hello', 'Python']

str_list = ['world', 'hello', 'Python', 'java']
new_str_list = sorted(str_list)
print(new_str_list)   # 输出 ['Python', 'hello', 'java', 'world']

# 对列表生成器进行降序排序
new_str_list = sorted(str_list, reverse=True)
print(new_str_list)   # 输出 ['world', 'java', 'hello', 'Python']
