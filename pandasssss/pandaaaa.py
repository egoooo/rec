import pandas as pd
import numpy as np

def printinfo(o,info=""):
   print(info)
   print(o)
   return;

# pandas.Series

data = np.array(['a','b','c','d'])
s = pd.Series(data)
printinfo(s,'从ndarray创建一个系列')

data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
printinfo(s,'从ndarray创建一个系列+索引')

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
printinfo(s,'从字典创建一个系列')
# 从字典创建一个系列
# a    0.0
# b    1.0
# c    2.0
# dtype: float64


data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
printinfo(s,'从字典创建一个系列+index')

# 从字典创建一个系列+index
# b    1.0
# c    2.0
# d    NaN
# a    0.0
# dtype: float64

s = pd.Series(5, index=[0, 1, 2, 3])
printinfo(s,'从标量创建一个系列')

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
printinfo(s[0],"从具有位置的系列中访问数据")
printinfo(s[:3],"从具有位置的系列中访问数据")
printinfo(s[-1:],"从具有位置的系列中访问数据")
printinfo(s['a'],"索引访问数据")
printinfo(s[['a','b','c']],"多个索引访问数据")

#Pandas数据帧（DataFrame）
data = [1,2,3,4,5]
df = pd.DataFrame(data)
printinfo(df,'从列表创建DataFrame')

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
printinfo(df,'从列表创建DataFrame+columns')
# 从列表创建DataFrame+columns
#      Name  Age
# 0    Alex   10
# 1     Bob   12
# 2  Clarke   13


data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
printinfo(df,'从列表创建DataFrame+columns+dtype')

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
printinfo(df,'从ndarrays/Lists的字典来创建DataFrame')
# 从ndarrays/Lists的字典来创建DataFrame
#     Name  Age
# 0    Tom   28
# 1   Jack   34
# 2  Steve   29
# 3  Ricky   42

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
printinfo(df,'从ndarrays/Lists的字典来创建DataFrame+index')

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
printinfo(df,'从字典列表创建数据帧DataFrame')
# 从字典列表创建数据帧DataFrame
#    a   b     c
# 0  1   2   NaN
# 1  5  10  20.0

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
printinfo(df,'从字典列表创建数据帧DataFrame+index')

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
printinfo(df1,"选择a，b")
printinfo(df2,"选择a，b1，没有b1")


d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
printinfo(df,'从系列的字典来创建DataFrame')
# 从系列的字典来创建DataFrame
#    one  two
# a  1.0    1
# b  2.0    2
# c  3.0    3
# d  NaN    4

printinfo(df['one'],'列选择')



print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
printinfo(df,'列添加')

print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']
printinfo(df,'列添加')

# using del function
print ("Deleting the first column using DEL function:")
del df['one']
printinfo(df,'列删除')

# using pop function
print ("Deleting another column using POP function:")
df.pop('two')
printinfo(df,'列删除+pop')


# loc需要两个单/列表/范围运算符，用","分隔。第一个表示行，第二个表示列。
df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
#select all rows for a specific column
printinfo(df)
printinfo(df.loc[:,'A'],' loc需要两个单/列表/范围运算符')

printinfo (df.loc['a']>0,'布尔类型行选择')


d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
printinfo(df.loc['b'],'行选择')
# 行选择
# one    2.0
# two    2.0



printinfo(df.iloc[0],'根据整数位置选择行')
# 根据整数位置选择行
# one    1.0
# two    1.0
# Name: a, dtype: float64

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
printinfo(df[2:4],'行切片')

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df = df.append(df2)
printinfo(df,'附加行')

df = df.drop(0)
printinfo(df,'删除行')

#系列基本功能
# 1	axes	返回行轴标签列表。
# 2	dtype	返回对象的数据类型(dtype)。
# 3	empty	如果系列为空，则返回True。
# 4	ndim	返回底层数据的维数，默认定义：1。
# 5	size	返回基础数据中的元素数。
# 6	values	将系列作为ndarray返回。
# 7	head()	返回前n行。
# 8	tail()	返回最后n行。

# DataFrame基本功能下面来看看数据帧(DataFrame)
# 1	T	转置行和列。
# 2	axes	返回一个列，行轴标签和列轴标签作为唯一的成员。
# 3	dtypes	返回此对象中的数据类型(dtypes)。
# 4	empty	如果NDFrame完全为空[无项目]，则返回为True; 如果任何轴的长度为0。
# 5	ndim	轴/数组维度大小。默认定义：2
# 6	shape	返回表示DataFrame的维度的元组。多少行，多少列
# 7	size	NDFrame中的元素数。
# 8	values	NDFrame的Numpy表示。
# 9	head()	返回开头前n行。
# 10	tail()	返回最后n行。

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}


df = pd.DataFrame(d)
print ("Our object is:")
printinfo(df,'pandas DataFrame')
print ("The actual data in our data frame is:")
printinfo(df.values,'NDarray')


#Pandas迭代

df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
print(df)
print('将每个列作为键，将值与值作为键和列值迭代为Series对象。')
for key,value in df.iteritems(): #列打印
   print (key,value)

print('产生每个索引值以及包含每行数据的序列。')
for row_index,row in df.iterrows():
   print (row_index,row)

print('itertuples()方法将为DataFrame中的每一行返回一个产生一个命名元组的迭代器。')
for row in df.itertuples():
    print (row)