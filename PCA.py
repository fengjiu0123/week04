# -*- coding: utf-8 -*-
# 使用PCA求样本矩阵X的K阶降维矩阵Zpython 实现PCA

import numpy as np
from sklearn.decomposition import PCA
class CPCA(object):                                # 定义一个名为CPCA的类，继承自object
    def __init__(self,K):                          # 初始化函数，接受一个参数 K，用于指定降维后的目标维度
        self.K = K                                 # 降维后目标矩阵的维度,将参数 K 存储在对象的属性self.K 中
    def fit_transform(self,X):                     # 定义一个方法 fit_transform，接受一个参数 K，用于拟合并转换数据
        X = X - X.mean(axis=0)                     # 对输入的数据 X 进行去中心化操作
        self.convariance = np.dot(X.T,X)/X.shape[0]      # 计算去中心化后数据的协方差矩阵
        a,b = np.linalg.eig(self.convariance)            # 使用numpy的线性代数工具计算协方差矩阵对的特征值和特征向量
        idx = np.argsort(-1 * a)                         # 对特征值进行降序排序，返回排序后的索引
        self.components = b[:,idx[:self.K]]              # 根据降序特征值选取前 K 个特征向量作为降序矩阵的组成部分
        return np.dot(X,self.components)                 # 将原始数据 X 投影到选定的主成分上，返回降维后的数据

if __name__=='__main__':                                # 判断当前文件是否作为主程序执行
    X = np.array([[10, 15, 29],                         # 10样本3特征的样本集, 行为样例，列为特征维度
                  [15, 46, 13],
                  [23, 21, 30],
                  [11, 9,  35],
                  [42, 45, 11],
                  [9,  48, 5],
                  [11, 21, 14],
                  [8,  5,  15],
                  [11, 12, 21],
                  [21, 20, 25]])
    K = np.shape(X)[1] - 1                       # 跟进样本集 x 的特征维度确定降维目标维度K
    print('样本集(10行3列，10个样例，每个样例3个特征):\n',X)     # 打印样本集 X
    pca_ = CPCA(K)                               # 创建CPCA类的实例pca_，传入降维目标维度K
    new_X = pca_.fit_transform(X)                 # 对样本集 X 进行降维处理，将结果保存到new_X中
    print(new_X)                                 # 打印降维后的数据 new_X
    pca = PCA(n_components=2)                    # 创建 sklearn 中的 PCA 类实例 pca，指定降维后的维度为 2
    pca.fit(X)                                   # 拟合 原始数据X
    pca_X = pca.fit_transform(X)                 # 将原始数据 X进行降维处理，结果保存在pca_X中
    print(pca_X)                                 # 打印sklearn 中PCA处理后的降维数据
















