import pandas as pd
import itertools as its
data = {'A': [1, 1, 2, 3, 5], 'B': [1, 2, 2, 3, 4],'C': [1, 2, 2, 3, 4],'D': [1, 2, 2, 3, 4]}
frame1 = pd.DataFrame(data)
print(frame1)

data1 = {'A': [1, 2, 3, 4],
         'B': [1, 1, 3, 5],
         'C': [1, 1, 3, 5],
         'E': [1, 1, 3, 5]
         }
frame2 = pd.DataFrame(data1)
print(frame2)

# 比较两个DataFrame

R = 110
T2 = []
k = 3
# 把前面k-1个特征实例编号取出来并且做比较
*feature1, temp_feature1 = list(frame1.columns)  # 取出第一个频繁模式特征
*feature2, temp_feature2 = list(frame2.columns)  # 取出第二个频繁模式特征
if (feature1 == feature2):  # 如果特征相等则比较实例编号
    temp_columns = list(frame1.columns)
    temp_columns.extend(temp_feature2)  # 创建一个DataFrame存放k阶的实例
    print(temp_columns)
    tempT_DataFrame = pd.DataFrame(columns=range(k))
    for i in range(len(frame1)):
        *X1, x1 = frame1.ix[i, :]  # 取出第一个频繁模式前k-1列的实例
        print(X1)
        for j in range(len(frame2)):
            *X2, x2 = frame2.ix[j, :]   # 取出第二个频繁模式前k-1列的实例
            print(X2)
            if (X1 == X2):  # 如果实例编号相等，则检测第k个实例是否满足R邻近或者频繁
                #distanceT = distance_instance(temp_feature1,x1,temp_feature2,x2)
                distanceT = 100
                if distanceT < R:
                    xx = list(frame1.ix[i, :])
                    xx.append(x2)  # 将第二个模式的最后一个实例编号放在第一个频繁模式的实例编号后面
                    tempT_Series = pd.Series(xx)
                    tempT_DataFrame = tempT_DataFrame.append(
                        tempT_Series, ignore_index=True)
                    print(tempT_DataFrame)
    # 检查tempT_DataFrame是否为空，不为空才存放
    if not tempT_DataFrame.empty:
        tempT_DataFrame.columns = temp_columns
        T2.append(tempT_DataFrame)
print(T2)


def distance_instance(E, temp_feature1, i1, temp_feature2, i2):
        # 计算两个实例之间的距离
    temp1 = E[E['Feature'] == temp_feature1]
    temp2 = temp1[temp1['ID'] == i1]
    x1 = float(temp2.ix[:, 'X-coordinate'])
    y1 = float(temp2.ix[:, 'Y-coordinate'])
    temp3 = E[E['Feature'] == temp_feature2]
    temp4 = temp3[temp3['ID'] == i2]
    x2 = float(temp4.ix[:, 'X-coordinate'])
    y2 = float(temp4.ix[:, 'Y-coordinate'])
    dist = distance.euclidean((x1, y1), (x2, y2))
    return dist
    ##
    # def fact(n):
    # if n==1:
    # return 1
    # return n * fact(n - 1)

    ##import itertools as its
    # ET=['A','B','C','D','E','F']
    ##tempCk = list(its.combinations(ET, 3))
    # print(tempCk)
    # for i in tempCk:
    ##    ET1 = list(i)
    ##    temp1 = list(its.combinations(ET1, 2))
    ##
    # print(temp1)
