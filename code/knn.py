# 根据跟癌症相关的一些数据来判断癌症的检测结果
# 能理解体会这个算法，但是对python的读取文件啊语法啊还有点陌生（python写起来有点丑）
# 读取写入csv文件，既能读取csv也能输出csv
import csv
with open('Prostate_Cancer.csv','r') as file:
# 以字典的形式读取文件
    reader=csv.DictReader(file)
# 将每一行的数据即不同id的一整行数据（相当于每个人的数据吧）抽出来放到datas里面
datas=[row for row in reader]

# 分组
# 将顺序打乱，减少数据偶然性
random.shuffle(datas)
# 训练集2/3 测试集1/3
# 下标是整数，所以不能直接/3要用整除
n=len(datas)//3
# n个是长度的1/3，所以测试集为第0个到第n个，训练集为第n个到最后
test_set=datas[0:n]
train_set=datas[n:]
print(test_set)
# KNN
# 距离
#将那些数据种类都整到一个元组里
# csv读过来的所有东西都是字符串，所有的东西不能直接相加减，要转成数据类型，数据里有小数，要用float
def distance(d1,d2):
    res=0    # 计算两个数据之间的欧式距离
    for key in ("radius","texture","perimeter","area","smoothness","compactness","symmetry","fractal_dimension"):
        res+=(float(d1[key])-float(d2[key]))**2
    return res**0.5

# K的取值要适中，太大也不行太小也不好，先取一个，后面可以换数字慢慢测准确率，测出一个高一些的
K=5
def knn(data):
    # 1.调用上面定义的计算距离的方法计算相关数据与训练集的距离
    res=[
        {"result":train['diagnosis_result'],"distance":distance(data,train)}
        for train in train_set
    ]
    #2. 对距离的远近进行排序——升序
    res=sorted(res,key=lambda item:item['distance'])
    # 3.取距离小的前k个
    res2=res[0:k]
    # 4.加权平均
    result={'B':0,'M':0}
    # 总距离
    sum=0
    for r in res2:
        sum+=r['distance']
        for r in res2:
            result[r['result']]+=1-r['distance']/sum
            if result['B']>result['M']:
                return 'B'
            else:
                return 'M'
            # 测试阶段
            # 成功的次数除以测试的总数测出准确率
            correct=0
            for test in test_set:
                result=test['diagnosis_result']
            result2=knn(test)
            if result==result2:
                correct+=1

                print("准确率：{：2f}%".format(100*correct/len(test_set)))





# 数据不够庞大，所有准确性不够高，但这个准确性相对来说很高了
