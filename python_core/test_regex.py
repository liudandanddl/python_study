#!/usr/bin/env python
# coding=utf-8
import re  # 正则表达式模块，对字符串截取替换功能强大

__author__ = 'ldd'
# *匹配0次或者多次    +匹配1次或者多次     ？匹配0次或者1次
simple_email = '\w+@\w+\.com'  # 简单电子邮件地址正则表达式 例如 1094684884@qq.com
common_email = '\w+@(\w+\.)*\w+\.com'  # 电子邮件地址，允许任意大于1数量的中间子域名存在 例如 nobody@www.xxx.yyy.com
num_float = '\d+(\.\d*)?'  # 表示简单浮点数的字符串，也就是说，任何十进制数字，例如‘0.004’，‘2’，‘75.’等

if __name__ == "__main__":
    pattern = r'.foo|on'
    m = re.match(pattern, 'afood on foo')  # 从字符串的起始部分对模式进行匹配，匹配成功就返回一个匹配对象，匹配失败返回None
    print(m, type(m))  # (<_sre.SRE_Match object at 0x108dab308>, <type '_sre.SRE_Match'>)
    if m is not None:
        print(m.group())  # 匹配成功，输出匹配内容,即pattern变量中匹配的内容  afoo

    print("--------------search------------")
    s = re.search(pattern, 'seafon in food')  # 搜索模式在字符串中第一次出现的位置，严格对字符串从左到右搜索
    print(s, type(s))  # (<_sre.SRE_Match object at 0x106583370>, <type '_sre.SRE_Match'>)
    if s is not None:  # 搜索到成功的匹配返回一个匹配对象，失败返回None
        print(s.group())  # on
    s = re.search(r'(?P<sdit>.foo|on)', 'seafon in food')
    print(s.groupdict())  # {'sdit': 'on'}

    print("---------------second-----------------")
    # 用()来匹配和保存子组，group(num=0)用于以普通方式str显示所有匹配部分，返回整个匹配对象或者编号为num的特定子组
    # groups()返回一个包含所有匹配子组的元组，如果没有成功匹配，则返回一个空元组
    p = '(\w{3})-(\d{3})'
    m1 = re.match(p, 'abc-12345')
    if m1 is not None:
        print(m1.group(), type(m1.group()), m1.group(0), m1.group(1), m1.group(2))  # ('abc-123', <type 'str'>, 'abc-123', 'abc', '123'
        print(m1.groups(), type(m1.groups()))  # (('abc', '123'), <type 'tuple'>)
    p2 = '(a(b))'
    m2 = re.match(p2, 'ab')
    print(m2.group(), m2.group(0), m2.group(1), m2.group(2))  # ('ab', 'ab', 'ab', 'b')
    print(m2.groups())  # ('ab', 'b')


    print("----------------匹配字符串的起始和结尾以及单词边界--------------")
    m3 = re.search(r'^The', 'The end.')
    if m3 is not None: print('One: ', m3.group())  # 匹配，在开始位置
    m3 = re.search(r'^The', 'end. The ')
    if m3 is not None: print('two: ', m3.group())  # 不匹配，不在开始位置
    m3 = re.search(r'The\b', 'end. sThe ')
    if m3 is not None: print('three: ', m3.group())  # 匹配，在单词右边界
    m3 = re.search(r'\bThe', 'end. aThe')
    if m3 is not None: print('four: ', m3.group())  # 不匹配，不在单词左边界
    m3 = re.search(r'\bThe', 'end. Theb')
    if m3 is not None: print('five: ', m3.group())  # 匹配，在左边界
    m3 = re.search(r'\bThe\b', 'end. The')
    if m3 is not None: print('six: ', m3.group())  # 匹配一个单独的单词，两边都在边界

    print("-----------------findall  finditer-----------------------")
    m4 = re.findall(r'(ab)|(cd)', 'abb cdd ab cd')
    print(m4, type(m4), m4.__len__())  # ([('ab', ''), ('', 'cd'), ('ab', ''), ('', 'cd')], <type 'list'>, 4)
    m4 = re.finditer(r'(ab)|(cd)', 'abb cdd ab cd', re.I)
    print(type(m4))  # <type 'callable-iterator'>迭代器
    for temp in m4:
        print(temp.group())

    print("-----------------sub()  subn()---------------------------")
    s1 = re.sub('X', 'LDD', 'attn:X Dear X, ', 1)  # 使用LDD替换字符串中的所有X，，除非定义count否则全部替换，count的默认值是0表示全部替换
    print(s1, type(s1))  # ('attn:LDD Dear X, ', <type 'str'>)
    s1 = re.subn('X', 'LDD', 'attn:X Dear X, ')
    # subn和sub的功能相同，只是结果返回的是一个tuple类型，替换后的字符串和表示替换总数的数字
    print(s1, type(s1))  # (('attn:LDD Dear LDD, ', 2), <type 'tuple'>)

    print("-----------------re.split()分割字符串--------------------------")
    # 与字符串使用split方法相比引入正则表达式会影响性能，但依赖正则表达式比字符串分割功能更强大
    sp1 = re.split(':', 'str1:str2:str3')
    print(sp1, type(sp1))  # (['str1', 'str2', 'str3'], <type 'list'>)

    print("------------------re扩展符号--标志表------------------------------------")
    ('\n'
     '    I = IGNORECASE 使匹配对大小写不敏感\n'
     '    L = LOCALE 做本地化识别(local-aware)匹配\n'
     '    U = UNICODE = sre_compile.SRE_FLAG_UNICODE # assume unicode locale\n'
     '    M = MULTILINE 多行匹配，影响 匹配字符串起始部分^ 和 匹配字符串终止部分$\n'
     '    S = DOTALL 使 . 匹配包括换行在内的所有字符\n'
     '    X = VERBOSE 能够使用REs的verbose状态，使之被组织得更清晰易懂\n'
     '    '
     )
    print(re.findall(r'(?i)yes', 'yes?Yes.YES,yEs'))  # ['yes', 'Yes', 'YES', 'yEs']
    strtemp = '''This line is the first\nanother line\nthat line\nit's the best\nthat a apple'''
    print(strtemp)
    print(re.findall(r'(?i)^th\w+', strtemp))  # ['This']
    print(re.findall(r'(?im)^th[\w *]*', strtemp))  # ['This line is the first', 'that line', 'that a apple']
    print(re.findall(r'(?i).*ne$', strtemp))  # []
    print(re.findall(r'(?im).*ne$', strtemp))  # ['another line', 'that line']

    print("---------------------(?=....)正向前视断言-----(?!....)负向前视断言------------")
    # 打印姓氏为 van Rossum的人的名字
    print(re.findall(r'\w+(?= van Rossum)', ''' Guido van Rossum\nTim Peters\nAlex Mar\nJust van Rossum'''))  # ['Guido', 'Just']
    stremail = '''sales@phptr.com\npostmaster@phptr.com\n   eng@phptr.com\nnoreply@phptr.com\nadmin@phptr.com'''
    # 忽略noreply或者postmaster开头的email地址
    pattern = r'(?m)^\s*(?!noreply|postmaster)(\w+)'
    print(re.findall(pattern, stremail))  # ['sales', 'eng', 'admin']
    pattern = r'(?m)^\s*(?!noreply|postmaster)(.+)'
    print(re.findall(pattern, stremail))  # ['sales@phptr.com', 'eng@phptr.com', 'admin@phptr.com']

    print("-------------贪婪操作符+*------非贪婪操作符？------------------------")
    # 贪婪操作符：试图获取匹配该模式尽可能多的字符
    # 非贪婪操作符：要求正则表达式引擎尽匹配可能少的字符
    data = 'Thu Feb 15 17:46:04 2007::uzi@dfd.gov::1171590364-6-8'
    print(re.match(r'.*(\d+-\d+-\d+)', data).group(1))  # 4-6-8
    print(re.match(r'.*?(\d+-\d+-\d+)', data).group(1))  # 1171590364-6-8