

- 了解线性方程组的求解过程

- 矩阵的运算（+-*）、求逆、

- 矩阵的秩，协方差、特征值与特征向量。

  一些有纸质笔记。一些来不及的就没有。拍照上传，照片放文件夹里。

  

  ##### 欧式距离

  欧式距离也称欧几里得距离，是最常见的距离度量，衡量的是多维空间中两个点之间的绝对距离。

  m维空间中两个点之间的真实距离，或者向量的自然长度（即该点到原点的距离）

  ![img](https://img-blog.csdnimg.cn/20190626150157233.png)

  样本的相似性度量

  这个计算公式很眼熟，以前学过好像

  适用于低维数据且向量的大小非常重要的时候

  ##### 闵氏距离

  是欧氏空间中的一种测度，被看做是欧氏距离的一种推广

  它是在范数向量空间（n 维实数空间）中使用的度量，这意味着它可以在一个空间中使用，在这个空间中，距离可以用一个有长度的向量来表示。

  ![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9LbVhQS0ExOWdXaWN5eERLUExOTG5tZFZvWXhSbTU5M1ByTzFEc245WjFlbVZOYmdMdklSekNtMDlWYjNOZU5vNVZQZlM3NTdpYWFPZUh5TU5wZjVEbVNRLzY0MA?x-oss-process=image/format,png)

  p=2的时候它就是欧式距离了

  ### 余弦值相似度

  即余弦距离，用向量空间中两个向量夹角的余弦值作为衡量两个个体间差异的大小的度量。

  余弦值越接近1，就表明夹角越接近0度，也就是两个向量越相似

  夹角越大相似度越低

  ##### 三角形中

  ![img](https://img-blog.csdn.net/20131111175208890)

  ##### 向量表示的三角形中

  ![img](https://img-blog.csdn.net/20131111175458906)

  ##### n维向量中

  ![img](https://img-blog.csdn.net/20131111175544093)

  总的来说就是把cos求出来，用夹角的大小来度量相似度。欧式距离是空间各点的绝对距离，跟各个点的位置坐标直接相关，

- ##### 了解中心化 ：Min-Max标准化

  是对原始数据进行线性变换，将值映射到[0,1]之间。

  ![image-20220120165614617](C:\Users\john\AppData\Roaming\Typora\typora-user-images\image-20220120165614617.png)

  算是一种规范化处理的方式之一。

- ##### Box-Cox转换。

  一种广义幂变换方法，是统计建模中常用的一种数据变换

  用于连续变量不满足正态分布的情况

  Box-Cox变换之后，可以一定程度上减小不可观测的误差和预测变量的相关性

  ![image-20220120164907650](C:\Users\john\AppData\Roaming\Typora\typora-user-images\image-20220120164907650.png)

  

   

- 了解统计知识：

  ##### t检验

  适用于计量资料、[正态分布](https://so.csdn.net/so/search?q=正态分布&spm=1001.2101.3001.7020)、方差具有齐性的两组间小样本比较。包括配对资料间、样本与均数间、两样本均数间比较三种。主要是用于小样本（样本容量小于30）的两个平均值差异程度的检验方法。对于两组定量样本的比较，若满足t检验的各项前提条件，使用t检验。

  

  ##### f检验

  用于方差分析。即对两个或两个以上样本率（构成比）进行差别比较的统计方法。

  ##### 正态检验

  Shapiro-Wilk正态检验方法来检验样本是否符合[正态分布](https://so.csdn.net/so/search?q=正态分布&spm=1001.2101.3001.7020)：

  ##### 卡方检验

  主要用于等级资料 ，在比较两个及两个以上样本率( 构成比）是否有差异 或 两个分类变量的关联性分析时用它

  ① n ≥40，T ≥ 5时，用Pearson卡方检验：

  ~~~python
  chisq.test(x)
  ~~~


  ② 当n≥40时，如果某个格子出现1≤T≤5，则需作连续性校正：

  ~~~python
  chisq.test(x, correct = TRUE)
  ~~~


  ③ n<40或任何格子出现T<1，或检验所得的P值接近于检验水准α，采用Fisher确切概率检验：

  ~~~python
  fisher.test(x)
  ~~~

  ##### 了解最小二乘法

最小二乘法（又称最小平方法）是一种数学优化技术。它通过最小化误差的平方和寻找数据的最佳函数匹配。利用最小二乘法可以简便地求得未知的数据，并使得这些求得的数据与实际数据之间误差的平方和为最小。最小二乘法还可用于曲线拟合。其他一些优化问题也可通过最小化能量或最大化熵用最小二乘法来表达。

简而言之，最小二乘法同梯度下降类似，都是一种求解无约束最优化问题的常用方法，并且也可以用于曲线拟合，来解决回归问题。

以前学过好像，用来求什么的有点忘了，好像是求零点范围？

最常用的是**普通最小二乘法（ Ordinary  Least Square，OLS）**：所选择的回归模型应该使所有观察值的残差平方和达到最小。

![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWFnZXMyMDE3LmNuYmxvZ3MuY29tL2Jsb2cvNTUzMDYyLzIwMTcwOS81NTMwNjItMjAxNzA5MTExNjQ2NDExMjUtNzY5ODQyOTQwLnBuZw?x-oss-process=image/format,png)



对这些算法什么的，只是了解，体会不太深，如果之后有应用到实际生活的某个例子上，感觉才能有更深的了解和体会。听说信管也要学算法，之后有机会应用再多点体会和学习吧。









### 提交目标

用Python编写函数：输⼊变量n，输出形如{1:1, … ,n: n*n} 的字典。例如当n=8时，输出{1: 1，2: 4, 3: 9, 4: 16, 5:25, 6: 36, 7: 49, 8: 64}

~~~python
n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i
    print(d)
~~~

