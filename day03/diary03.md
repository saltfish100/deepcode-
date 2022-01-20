# Python基础语法

### 数据类型

##### Numbers

(int Long float complex)                 

complex由实数和虚数构成，可以用a+bj或者complex(a,b)表示，a和b都是浮点型

> **注意：**long 类型只存在于 Python2.X 版本中，在 2.2 以后的版本中，int 类型数据溢出后会自动转为long类型。在 Python3.X 版本中 long 类型被移除，使用 int 替代。

##### String 

由数字、字母、下划线组成的一串字符，表示文本。

python的字串列表有2种取值顺序:

- 从左到右索引默认0开始的，最大范围是字符串长度少1

- 从右到左索引默认-1开始的，最大范围是字符串开头

  要实现从字符串中获取一段子字符串的话，可以使用 **[头下标:尾下标]** 来截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。

  ```python
  >>> s = 'abcdef'
  >>> s[1:5]
  'bcde
  ```

加号（+）是字符串连接运算符，星号（*）是重复操作。*几就是重复操作几次。

Python 列表截取可以接收第三个参数，参数作用是截取的步长。

~~~python
letters = 'checkio'
letters[1:4:2]=['h','c']
~~~



### 列表(列表表达式)

有序的对象集合，偏移存取，可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。

~~~python
print list               # 输出完整列表                 print list[0]            # 输出列表的第一个元素  

print list[1:3]          # 输出第二个至第三个元素              print list[2:]           # 输出从第三个开始至列表末尾的所有元素

 print tinylist * 2       # 输出列表两次                     print list + tinylist    # 打印组合的列表

//列表的更新

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]            list[2] = 1000

list = []          ## 空列表
list.append('Google')   ## 使用 append() 添加元素
del list1[2]             ##删除列表的元素
~~~

| Python 表达式                | 结果                         | 描述                 |
| :--------------------------- | :--------------------------- | :------------------- |
| len([1, 2, 3])               | 3                            | 长度                 |
| [1, 2, 3] + [4, 5, 6]        | [1, 2, 3, 4, 5, 6]           | 组合                 |
| ['Hi!'] * 4                  | ['Hi!', 'Hi!', 'Hi!', 'Hi!'] | 重复                 |
| 3 in [1, 2, 3]               | True                         | 元素是否存在于列表中 |
| for x in [1, 2, 3]: print x, | 1 2 3                        | 迭代                 |

| 序号 | 函数                                                         |
| :--- | :----------------------------------------------------------- |
| 1    | [cmp(list1, list2)](https://www.runoob.com/python/att-list-cmp.html) 比较两个列表的元素 |
| 2    | [len(list)](https://www.runoob.com/python/att-list-len.html) 列表元素个数 |
| 3    | [max(list)](https://www.runoob.com/python/att-list-max.html) 返回列表元素最大值 |
| 4    | [min(list)](https://www.runoob.com/python/att-list-min.html) 返回列表元素最小值 |
| 5    | [list(seq)](https://www.runoob.com/python/att-list-list.html) 将元组转换为列表 |

| 序号 | 方法                                                         |
| :--- | :----------------------------------------------------------- |
| 1    | [list.append(obj)](https://www.runoob.com/python/att-list-append.html) 在列表末尾添加新的对象 |
| 2    | [list.count(obj)](https://www.runoob.com/python/att-list-count.html) 统计某个元素在列表中出现的次数 |
| 3    | [list.extend(seq)](https://www.runoob.com/python/att-list-extend.html) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） |
| 4    | [list.index(obj)](https://www.runoob.com/python/att-list-index.html) 从列表中找出某个值第一个匹配项的索引位置 |
| 5    | [list.insert(index, obj)](https://www.runoob.com/python/att-list-insert.html) 将对象插入列表 |
| 6    | [list.pop([index=-1\])](https://www.runoob.com/python/att-list-pop.html) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 |
| 7    | [list.remove(obj)](https://www.runoob.com/python/att-list-remove.html) 移除列表中某个值的第一个匹配项 |
| 8    | [list.reverse()](https://www.runoob.com/python/att-list-reverse.html) 反向列表中元素 |
| 9    | [list.sort(cmp=None, key=None, reverse=False)](https://www.runoob.com/python/att-list-sort.html) 对原列表进行排序 |

### 元组Tuple

元组用 **()** 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表.

输出方式和list差不多。

~~~python
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )

print tuple               # 输出完整元组                           ('runoob', 786, 2.23, 'john', 70.2)

 print tuple[0]            # 输出元组的第一个元素                runoob

tinytuple = (123, 'john')          

print tinytuple * 2       # 输出元组两次                (123, 'john', 123, 'john')

print tuple + tinytuple   # 打印组合的元组                      ('runoob', 786, 2.23, 'john', 70.2, 123, 'john')
~~~

列表和元组语法啥的差不多，结合起来。

元组不允许更新、修改！但可以进行连接组合。

元组中只包含一个元素时，需要在元素后面添加逗号

```python
tup1 = (50,)
```

元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组          del tup

| Python 表达式                | 结果                         | 描述         |
| :--------------------------- | :--------------------------- | :----------- |
| len((1, 2, 3))               | 3                            | 计算元素个数 |
| (1, 2, 3) + (4, 5, 6)        | (1, 2, 3, 4, 5, 6)           | 连接         |
| ('Hi!',) * 4                 | ('Hi!', 'Hi!', 'Hi!', 'Hi!') | 复制         |
| 3 in (1, 2, 3)               | True                         | 元素是否存在 |
| for x in (1, 2, 3): print x, | 1 2 3                        | 迭代         |

任意无符号的对象，以逗号隔开，默认为元组

### 字典Dictionary

无序的对象集合，字典当中的元素是通过键来存取的。

字典用"{ }"标识。字典由索引(key)和它对应的值value组成。

```python
dict['one'] = "This is one"      print dict['one']          # 输出键为'one' 的值         This is one

tinydict = {'name': 'runoob','code':6734, 'dept': 'sales'}

print tinydict.keys()      # 输出所有键             print tinydict.values()    # 输出所有值
['dept', 'code', 'name']                            ['sales', 6734, 'runoob']

 
tinydict['Age'] = 8 # 更新
tinydict['School'] = "RUNOOB" # 添加
```

字典值可以没有限制地取任何 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住。

键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行。

| 序号 | 函数及描述                                                   |
| :--- | :----------------------------------------------------------- |
| 1    | [cmp(dict1, dict2)](https://www.runoob.com/python/att-dictionary-cmp.html) 比较两个字典元素。 |
| 2    | [len(dict)](https://www.runoob.com/python/att-dictionary-len.html) 计算字典元素个数，即键的总数。 |
| 3    | [str(dict)](https://www.runoob.com/python/att-dictionary-str.html) 输出字典可打印的字符串表示。 |
| 4    | [type(variable)](https://www.runoob.com/python/att-dictionary-type.html) 返回输入的变量类型，如果变量是字典就返回字典类型。 |

| 序号 | 函数及描述                                                   |
| :--- | :----------------------------------------------------------- |
| 1    | [dict.clear()](https://www.runoob.com/python/att-dictionary-clear.html) 删除字典内所有元素 |
| 2    | [dict.copy()](https://www.runoob.com/python/att-dictionary-copy.html) 返回一个字典的浅复制 |
| 3    | [dict.fromkeys(seq[, val\])](https://www.runoob.com/python/att-dictionary-fromkeys.html) 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值 |
| 4    | [dict.get(key, default=None)](https://www.runoob.com/python/att-dictionary-get.html) 返回指定键的值，如果值不在字典中返回default值 |
| 5    | [dict.has_key(key)](https://www.runoob.com/python/att-dictionary-has_key.html) 如果键在字典dict里返回true，否则返回false |
| 6    | [dict.items()](https://www.runoob.com/python/att-dictionary-items.html) 以列表返回可遍历的(键, 值) 元组数组 |
| 7    | [dict.keys()](https://www.runoob.com/python/att-dictionary-keys.html) 以列表返回一个字典所有的键 |
| 8    | [dict.setdefault(key, default=None)](https://www.runoob.com/python/att-dictionary-setdefault.html) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default |
| 9    | [dict.update(dict2)](https://www.runoob.com/python/att-dictionary-update.html) 把字典dict2的键/值对更新到dict里 |
| 10   | [dict.values()](https://www.runoob.com/python/att-dictionary-values.html) 以列表返回字典中的所有值 |
| 11   | [pop(key[,default\])](https://www.runoob.com/python/python-att-dictionary-pop.html) 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。 |
| 12   | [popitem()](https://www.runoob.com/python/python-att-dictionary-popitem.html) 返回并删除字典中的最后一对键和值。 |

### 循环语句

这这这和其他语言挺像的

##### while

```python
while 判断条件：
    执行语句(statements)……
else：
     执行语句
    continue 用于跳过该次循环，break 则是用于退出循环
```

无限循环：如果条件判断语句永远为 true，循环将会无限的执行下去。

无限循环可以使用 CTRL+C 来中断循环。

##### for

~~~python
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ('%d 是一个质数' % num)
/*10 等于 2 * 5
11 是一个质数
12 等于 2 * 6
13 是一个质数
14 等于 2 * 7
15 等于 3 * 5
16 等于 2 * 8
17 是一个质数
18 等于 2 * 9
19 是一个质数*/
~~~

##### 嵌套循环

##### break 语句

用来终止循环语句，是用于退出整个循环。

##### continue

continue 语句跳出本次循环

后面不用加；号

### 函数

可以自己创建函数，这被叫做用户自定义函数。

##### 定义一个函数

- 函数代码块以 **def** 关键词开头，后接函数标识符名称和圆括号**()**。

- 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。

- 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。

- 函数内容以冒号起始，并且缩进。

- **return [表达式]** 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

  ~~~python
  def functionname( parameters ):
     "函数_文档字符串"
     function_suite
     return [expression]
  ~~~

  ~~~python
  def printme( str ):
     "打印传入的字符串到标准显示设备上"
     print str
     return
   //调用函数
  printme("我要调用用户自定义函数!")
  printme("再次调用同一函数")
  //输出结果：
  我要调用用户自定义函数!
  再次调用同一函数
  ~~~

  注意一下可变类型和不可变类型的更新

  python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

  ##### 必备参数

  必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

  调用printme()函数，你必须传入一个参数，不然会出现语法错误

  ##### 关键字参数

  关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。

  ~~~python
  def printme( str ):
     "打印任何传入的字符串"
     print str
     return
   
  #调用printme函数
  printme( str = "My string")
  ~~~

  ##### 默认参数

  调用函数时，默认参数的值如果没有传入，则被认为是默认值。

  如括号里有两个键，但传值只传了一个则默认没传的那个为原来的值。

  ##### 匿名函数

  python 使用 lambda 来创建匿名函数。

  - lambda只是一个表达式，函数体比def简单很多。
  - lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
  - lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
  - 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

  ### 模块

Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。模块能定义函数，类和变量，模块里也能包含可执行的代码。

~~~python

def print_func( par ):
   print "Hello : ", par
   return
~~~

##### 模块的引入

```python
import module1[, module2[,... moduleN]]
```

导入模块要把命令放在脚本的顶端。一个模块只会被导入一次。

**调用** math 模块中的函数时，必须这样引用：

模块名.函数

##### from…import 语句

Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中

例如，要导入模块 fib 的 fibonacci 函数，使用如下语句：

```
from fib import fibonacci
```

这个声明不会把整个 fib 模块导入到当前的命名空间中，它只会将 fib 里的 fibonacci 单个引入到执行这个声明的模块的全局符号表。



把一个模块的所有内容全都导入到当前的命名空间

```
from modname import *
```

##### 命名

如果要给函数内的全局变量赋值，必须使用 global 语句。

------

##### dir()函数

dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。

返回的列表容纳了在一个模块里定义的所有模块，变量和函数。

##### globals() 和 locals() 函数

根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。

如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。

如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。

两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。

##### reload() 函数

当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块。

~~~python
reload(module_name)
~~~

# Knn算法

数据挖掘分类技术中的算法之一，其指导思想是”近朱者赤，近墨者黑“，即由你的邻居来推断出你的类别。

##### 实现原理

为了判断未知样本的类别，以所有已知类别的样本作为参照，计算未知样本与所有已知样本的距离，从中选取与未知样本距离最近的K个已知样本，根据少数服从多数的投票法则，将未知样本与K个最邻近样本中所属类别占比较多的归为一类。

##### 通用步骤

- 计算距离（常用欧几里得距离或马氏距离）

- 升序排列

- 取前k个

- 加权平均

  ##### K的选取（核心）

  K这个字母的含义就是要选取的最邻近样本实例的个数

  K的大小与结果的准确性呈正态分布

- k太大：导致分类模糊，离的太远，易引起欠拟合

- k太小：受个例影响，波动较大

  ##### 如何选取k

  - 经验

  - 均方根误差

    ##### 优点
    
    ​      1.简单，易于理解，易于实现，无需估计参数，无需训练；
    
    ​      2. 适合对稀有事件进行分类；
    
    ​      3.特别适合于多分类问题,对象具有多个类别标签
    
    ##### 缺点
    
    - 当样本不平衡时，有可能导致当输入一个新样本时，该样本的K个邻居中大容量类的样本占多数。
    
    采用加权平均的方法即和该样本距离小的邻居权值大来解决这个问题。
    
    - 计算量较大