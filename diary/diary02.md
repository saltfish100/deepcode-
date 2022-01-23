

# Day2——1.18

## Leetcode每日三题

- 349.两个数组的交集：[https://leetcode-cn.com/problems/intersection-of-two-arrays/](https://leetcode-cn.com/problems/intersection-of-two-arrays/)

  ##### 解题思路：

  用两个for循环遍历两个数组，再用if判断两个数是否相等，

  ##### 题解：

  ~~~java
  class Solution {
  
    public int[] intersection(int[] nums1, int[] nums2) {
  
  
  
  ​    Set<Integer> set = new HashSet();
  
  ​    for(int i = 0; i < nums1.length; i++){
  
  ​      for(int j = 0; j < nums2.length; j++){
  
  ​        if(nums1[i] == nums2[j]){
  
  ​          set.add(nums1[i]);
  
  ​        }
  
  ​      }
  
  ​    }
  
  ​    int[] res = new int[set.size()];
  
  ​     int j = 0;
  
  ​    for(int i : set){
  
  ​      res[j++] = i;
  
  ​    }
  
    return res;
  
    }
  
  }
  ~~~

  

- 88.合并两个有序数组：https://leetcode-cn.com/problems/merge-sorted-array/

  ##### 解题思路：

  将数组 *nums*2 放进数组 nums1 的尾部，

  ##### 题解

  ~~~javascript
   for (int i = 0; i != n; ++i) {
              nums1[m + i] = nums2[i];
          }
          Arrays.sort(nums1);
      }
  ~~~

  

- 234.回文链表：[https://leetcode-cn.com/problems/palindrome-linked-list/](https://leetcode-cn.com/problems/palindrome-linked-list/)

  没啥思路说实话，来不及学数据结构了

## JS

解释性语言,运行之前不需要编译，不会检查错误。严格区分大小写，其他的和其他语言区别不大。

### 基本语法

三种引入方式和css的差不多

~~~js
<script src=""> </script>
~~~

#### 变量

~~~语言
var 变量名 = 变量值
console.log(变量名);//会输出变量值，如果括号里面输入的内容加入了双引号，则输出的是双引号里面的内容。
var 变量名1= ，变量名2= ，变量名3= ；//简写方式
变量定义完没赋值则称为未初始化的变量，输出值为underfined
~~~

命名规则和Java的差不多，不能以数字开头，使用合成词时第一个单词全小写，第二个单词开始首字母大写

变量未被定义直接打印结果错误。

=出现的话将右边的东西赋值给左边

#### 数据类型

number类型 string类型 boolean类型  undefined（①声明变量未赋值；②访问对象不存在的属性）未定义

#### 数据类型转换

##### 隐式转换

①函数    typeof（）或typeof

~~~javascript
var num1 = 15;
var s = typeof(num1);
var s1 = typeof num1;
~~~

②NaN

isNaN（数据）：判断数据是否为非数字//结果为布尔型

注：所有的数据类型与string做+运算时最后的结果都为string

##### 强制转换

①toString（）将任意类型的数据转换为string类型

~~~javascript
var num = 15;
var str = num +"";
~~~

②parseInt() 获取指定数据的整数部分

`var result = parseInt(数据)`

从左向右转换，碰到第一个非整数字符则停止转换。如果第一个字符就是非整数字符的话结果为NaN

③parseFloat()将指定数据转换成小数

`var result = parseFloat(数据)`

④Number()将一个字符串解析为number

`var result = Number(数据)`

如果包含非法字符串则返回NaN

#### 函数

有点像Java中的方法，然后可以被调用

~~~javascript
function sayHello(userName,userPwd){
    可执行语句
    console.log(....)
}
//调用
sayHello(`Tom`,`123`);
~~~

~~~javascript
function add(num1,num2){
    return num1 + num2;
}
var result = add(10,20);
console.log(result);
~~~

函数作用域中的变量只在当前函数中可以被访问到，离开此范围就无法访问。

##### 声明提前

js执行时会将var声明的变量和function声明的函数预读到所在作用域顶部，但是对变量的赋值还保留在原来的位置。

//如果声明和赋值分开，输出在声明之前，需要注意一下这个点。

##### 按值传递

在函数体内对变量进行修改，不会影响到外部的实参变量。



#### 对象

Object

如果使用基本数据类型的数据，我们所创建的变量都是独立的，不能成为一个整体。

对象属于一种复合的数据类型，在对象中可以保存多个不同数据类型的属性。

##### ①内建对象

由ES标准中定义的对象，在任何的ES的实现中都可以实现

比如：Math String Number

##### ②宿主对象

由JS的运行环境提供的对象，目前来讲主要指由浏览器提供的对象

比如BOM DOM

##### ③自定义对象

由开发人员自己创建的对象



//在对象中保存的值称为属性，向对象添加属性

语法：对象.属性名=属性值

**添加**属性  obj.age = 18；

**读取**对象中的属性 console.log(obj.age);

//如果读取对象中没有的属性不会报错，会返回undefined

**修改**：对象.属性名=新值

**删除**：delete 对象.属性名

使用**特殊**的属性名：  对象["属性名"]=属性值                 读取时也采用这种方式

[]号的方式会很灵活

obj["123"] = 789;     var n = "123";     console.log(obj["123"]);

**in**运算符：检查一个对象中是否含有指定的属性           "属性名" in 对象

#### 作用域（作用域链）



#### BOM



#### DOM

对网页进行增删改查操作

##### 查找

1.按id属性，精确查找一个元素对象   GETElementByld("id")

只能用在document上，只用于查找一个元素，不是所有元素都有id

![id](C:\Users\john\Desktop\deepcode\day02\diary02.assets\id.png)

2.按标签名查找

可用在任意父元素上，而且查找所有子代节点。返回一个动态集合。即使只找到一个元素，也返回集合，要用[0]取出

![标签名](C:\Users\john\Desktop\deepcode\day02\diary02.assets\标签名.png)

![微信截图_20220118173040](C:\Users\john\Desktop\deepcode\day02\diary02.assets\微信截图_20220118173040-16424987845481.png)

3.通过name属性查找

![name](C:\Users\john\Desktop\deepcode\day02\diary02.assets\name.png)

4.通过class查找

![class](C:\Users\john\Desktop\deepcode\day02\diary02.assets\class.png)

![class2](C:\Users\john\Desktop\deepcode\day02\diary02.assets\class2.png)

5.通过css选择器查找

①只找一个元素

②找多个元素

![选择器](C:\Users\john\Desktop\deepcode\day02\diary02.assets\选择器.png)

##### 修改

①修改属性



### <img src="C:\Users\john\Desktop\deepcode\day02\diary02.assets\DOM1.png" alt="DOM1" style="zoom: 33%;" />

- <img src="C:\Users\john\Desktop\deepcode\day02\diary02.assets\DOM2-16425000312972.png" alt="DOM2" style="zoom: 33%;" />
  
  <img src="C:\Users\john\Desktop\deepcode\day02\diary02.assets\DOM3.png" alt="DOM3" style="zoom: 33%;" /><img src="C:\Users\john\Desktop\deepcode\day02\diary02.assets\DOM4-16425002792963.png" alt="DOM4" style="zoom:33%;" />
  
  - <img src="C:\Users\john\Desktop\deepcode\day02\diary02.assets\修改样式.png" alt="DOM4" style="zoom: 33%;" />②修改样式
  
    
  
    ##### 添加
  
    添加元素的步骤
  
    ①创建空元素
  
    var elem = document.createElement("元素名")
  
    ②设置关键属性
  
    ​	设置关键样式
  
    ③将元素添加到DOM树
  
    添加元素优化
  
    ### 困惑
  
    学的有点囫囵吞枣，只是学了一些知识点，知道是什么，学完的时候还是有点懵，不知道怎么和之前学的相结合，感觉跟在学Java一样，就是语法有点区别。在跟着网课的轮播图走了一遍之后（虽然也不知道代码哪里写错了，写到那里的时候up都能有轮播的效果了，我的按钮就没了），有点知道该怎么用了。后面再多花点时间看一些带习题讲解的网课吧，目标的地方基本上能实现或者说大部分知道该怎么弄。一两天时间学js太快了。
