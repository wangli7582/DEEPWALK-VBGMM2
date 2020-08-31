首先使用嵌入表示算法DeepWalk将高维网络嵌入到低维空间；
然后，使用变分贝叶斯高斯混合模型（VBGMM）将低维空间中的节点进行聚类。
优点：使用变分聚类所得到的社区个数无需事先指定，在自己构造的网络上所得到的NMI指标很高，接近1。

===============================
Ⅰ.  LFR   (参考论文《DeepWalk》)
===============================



===============================
Ⅰ.  DeepWalk   (参考论文《DeepWalk》)
===============================

1. 安装：
------------
#. cd deepwalk
#. pip install -r requirements.txt 
#. python setup.py install



2.一组参数的运行
-----------------
# deepwalk --format mat --input example_graphs/blogcatalog.mat --max-memory-data-size 0 --number-walks 80 --representation-size 128 --walk-length 40 --window-size 10 --workers 1 --output example_graphs/blogcatalog.embeddings

* 根据我们使用的网络的格式调整format后面的参数，有三种类型：.mat、默认.adjlist、.edgelist
input后面是输入的网络的路径，output后面是输出的.embeddings文件的路径


3.多组参数的运行
------------------
# python start.py

* 运行时间较长，会得到6*6*4*6个embedding文件，可以根据自己的需要调整代码。

===============================
Ⅱ.  VBGMM 
===============================
1.计算不同参数对应的NMI数值
----------------------------
# python preCommunity2.py

* 运行start.py之后，再运行该文件，可以得到一个VBGMM_result.txt文件，里面包含了不同的参数及其对应的NMI指标的数值。
格式例如：1v4v20v5     我们使用‘v’间隔四组影响参数

2.找到最优解
---------------------------
# python maxResult.py

3.画NMI随参数变化曲线
----------------------------
# python draw.py



4.得到网络划分结果图
-----------------------------
# python predCommunity.py


