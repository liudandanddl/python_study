#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'
import re

s = '38x1x234x35x612x3yxxx'

patten1 = re.compile("x.*x")  # 返回一个,中间重复x
# print('1\n',patten1.findall(s))  # ['x1x234x35x612x3yxxx']
patten2 = re.compile("x\w.*?x")  # 中间至少有一个字符.xx不行
# print('2\n',patten2.findall(s))  # ['x1x', 'x35x', 'x3yx']
patten3 = re.compile("x.*?x")  # 返回多个.不重复
# print('3\n',patten3.findall(s))  # ['x1x', 'x35x', 'x3yx', 'xx']
patten4 = re.compile("x+(.*?[xy])")  # 以x开头但开头不包含x,结尾以x或y结束
# print('4\n',patten4.findall(s))  # ['1x', '35x', '3y', 'x']


pattern = re.compile(r'hello')
res1 = re.match(pattern, 'hello')
print('res1:', res1.group())  # ('res1:', 'hello')

res2 = re.match(pattern, 'bhello hello')
print('res2:', res2)  # ('res2:', None)
res2 = re.search(pattern, 'bhello hello')
print('res2:', res2.group())  # ('res2:', 'hello')

res3 = re.match(pattern, 'hello hellob')
print('res3:', res3.group())  # ('res3:', 'hello')

pattern = re.compile(r'\d+')
res = re.split(pattern,'one1two2three3four4')
print(res, type(res))   # (['one', 'two', 'three', 'four', ''], <type 'list'>)

pattern = re.compile(r'\d+')
res = re.findall(pattern,'one1two2three3four4')
print(res, type(res))   # (['1', '2', '3', '4'], <type 'list'>)

pattern = re.compile(r'\d+')
for m in re.finditer(pattern,'one1two2three3four4'):
  print m.group(),  # 1 2 3 4

# m = re.match(r"(\w+) (\w+)", 'hello world!')
#
# print "m.string:", m.string  # 匹配时使用的文本
# print "m.re:", m.re  # 匹配时使用的Pattern对象
# print "m.pos:", m.pos  # 文本中正则表达式开始搜索的索引
# print "m.endpos:", m.endpos  # 文本中正则表达式结束搜索的索引
# print "m.lastindex:", m.lastindex  # 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
# print "m.lastgroup:", m.lastgroup  # 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。
# print "m.group():", m.group()  # 获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
# print "m.group(1,2):", m.group(1, 2)
# print "m.groups():", m.groups()  # 以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None
# print "m.groupdict():", m.groupdict()  #  返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。
# print "m.start(2):", m.start(2)
# print "m.end(2):", m.end(2)
# print "m.span(2):", m.span(2)
# print r"m.expand(r'\g \g'):", m.expand(r'\2 \1')