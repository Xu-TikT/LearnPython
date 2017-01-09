the_world_is_flat = False
if the_world_is_flat:
    print ("be careful not to fall off")
else:
    print ("here you are")

# 测试内存中变量的存储方式
#一开始a,b都指向10，之后a指向了5，而b不变
a = 10
b = a
a = 5
print (a)
print (b)

#打印多行字符串,如果要表示多行字符串，可以用'''...'''表示
#此方法效果等同于 'Line 1\nLine 2\nLine 3'
print ('''第一行
第二行
第三行''')

#如果一个字符串包含很多需要转义的字符，对每一个字符都进行转义会很麻烦。
# 为了避免这种情况，我们可以在字符串前面加个前缀 r ，表示这是一个 raw 字符串，里面的字符就不需要转义了。
print ('\(~_~)/\(~_~)/')
#但是r'...'表示法不能表示多行字符串，也不能表示包含'和 "的字符串。所以这个时候要和'''...'''组合使用
print (r'''Python is created by "Guido".
It is free and easy to learn.
Let's start learn Python in imooc!''')

print (r'he said "OK"')
print (r'''''''"hahaha''')

#布尔运算，Python使用 and, or, not来进行与或非的运算
#Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True
#True and 'a=T' 计算结果是 'a=T' 继续计算 'a=T' or 'a=F' 计算结果还是 'a=T'
a = True
print (a and 'a=T' or 'a=F')

#打印list数组,python中的数组元素可以是不同的数据类型
#L = ['Michael', 100, True]
#空数组：empty_list = []
L = ['Adam', 95.5, 'Lisa', 85, 'Bart', 59]
print (L)
#数组中使用负数下标代表倒序索引？
print (L[-1])
print (L[-2])
