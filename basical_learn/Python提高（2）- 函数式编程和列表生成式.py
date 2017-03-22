
# coding: utf-8

# ## 【Python提高（2）】函数式编程和列表生成式

# 迭代器和解析是一种神奇的东西，学会他们可以大大加快我们的工作速度，下面开始

# ## 一、常见的几种迭代器
# 
# 迭代器在python中是以C语言的速度运行的，而while循环版本则是通过Python虚拟机运行Python字节码的。
# 
# 1. range
# 
# 2. zip
# 可以让我们使用for循环来并行使用多个序列，zip会取得一个或多个序列为参数，然后返回元组的列表，将这些序列中的并排的元素配成对。
# 
# 3. enumerate
# 可以获得元素和元素的偏移值
# 
# 4. map
# map会对一个序列对象中的每一个元素应用被传入的函数，并且返回一个包含所有函数调用结果的一个列表。
# 
# 5. filter
# 基于某一测试函数过滤出一些元素
# 
# 6. reduce
# 对每对元素都应用函数并运行到最后结果

# ### 1、 range

# In[2]:

X = 'spam'
for i in range(len(X)):
    print (X[i])


# In[3]:

S = 'abcdefghijk'
for i in range(0,len(S),2):
    print S[i]


# #### 下面方法更容易理解，但是会复制一个字符串，如果字符串很大，占用内存较大

# In[4]:

S = 'abcdefghijk'
for c in S[::2]:
    print c   


# ### 2、 zip

# 结合zip实现并行遍历

# In[20]:

L1 = [1,2,3,4]
L2 = [5,6,7,8]
for (x,y) in zip(L1,L2):
    print (x,y,x+y)


# 使用zip构造字典

# In[3]:

keys = ['a','b','c']
vals = [1,3,5]
D2 = {}
for (k,v) in zip(keys,vals): D2[k]=v
D2


# ### 3、 enumerate
# 
# 可以获得元素和元素的偏移值

# In[1]:

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
dict(enumerate(seasons, start=3))


# ### 4、 map
# 
# map会对一个序列对象中的每一个元素应用被传入的函数，并且返回一个包含所有函数调用结果的一个列表。
# 
# map对每一个元素都应用了函数调用而不是任意的表达式，所以不太通用，但是在某些情况下，map比列表解析运行起来速度更快

# In[1]:

S1 = 'abc'
S2 = 'xyz123'
map(None,S1,S2)


# In[7]:

map(pow,[1,2,3],[2,3,4])


# In[8]:

map((lambda x: x+3),[1,2,3,4])


# In[10]:

def inc(x):
    return x+10
map(inc,[1,2,3])


# In[23]:

import math
list(map(math.sqrt,(x ** 2 for x in range(4))))


# ### 5、 filter
# 
# 基于某一测试函数过滤出一些元素

# In[11]:

list(filter((lambda x:x>0),range(-5,5)))


# ### 6、reduce
# 
# 对每对元素都应用函数并运行到最后结果

# In[12]:

reduce((lambda x,y:x+y),[1,2,3,4])


# In[13]:

import operator,functools
functools.reduce(operator.add,[2,4,6])


# ## 二、列表推导式
# 列表推导式为从序列中创建列表提供了一个简单的方法。普通的程序通过将一些操作应用于序列的每个成员并通过返回的元素创建列表，或者通过满足特定条件的元素创建子序列。
# 
# 例如，假设我们创建一个 squares 列表，可以像下面方式:

# In[5]:

squares = []
for x in range(10):
     squares.append(x**2)
squares


# 我们同样能够达到目的采用下面的方式:

# In[6]:

squares = [x**2 for x in range(10)]
squares


# 这也相当于 squares = map(lambda x: x**2, range(10))，但是上面的方式显得简洁以及具有可读性。
# 
# 列表推导式由包含一个表达式的括号组成，表达式后面跟随一个 for 子句，之后可以有零或多个 for 或 if 子句。结果是一个列表，由表达式依据其后面的 for 和 if 子句上下文计算而来的结果构成。
# 
# 例如，如下的列表推导式结合两个列表的元素，如果元素之间不相等的话:

# In[7]:

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


# In[8]:

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
         if x != y:   
            combs.append((x, y))
combs


# In[9]:

vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]


# In[10]:

[x for x in vec if x >= 0]


# In[11]:

[abs(x) for x in vec]


# In[12]:

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]


# In[13]:

[(x, x**2) for x in range(6)]


# In[14]:

vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]


# 列表推导式可使用复杂的表达式和嵌套函数:

# In[15]:

from math import pi
[str(round(pi, i)) for i in range(1, 6)]


# ##  三、嵌套的列表推导式
# 列表推导式可以嵌套。
# 
# 考虑以下的 3x4 矩阵，一个列表中包含三个长度为4的列表:

# In[16]:

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]


# 现在，如果你想交换行和列，可以用嵌套的列表推导式:

# In[17]:

[[row[i] for row in matrix] for i in range(4)]


# 像前面看到的，嵌套的列表推导式是对 for 后面的内容进行求值，所以上例就等价于:

# In[18]:

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
transposed


# 反过来说，如下也是一样的:

# In[19]:

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
transposed


# 在实际中，可以使用内置函数组成复杂流程语句。对此种情况 zip() 函数将会做的更好:

# In[20]:

list(zip(*matrix))


# 代码中使用的星号的说明，参数列表的分拆。
# 当要传递的参数已经是一个列表，但要调用的函数却只接受分开一个个的参数值。这时候需要把已有的列表拆开来。例如内建函数 range() 需要独立的 start ，stop 参数，可以在调用函数时加一个 * 操作符来自动把参数列表拆开

# In[ ]:



