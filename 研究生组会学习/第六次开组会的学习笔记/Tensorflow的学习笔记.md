# Tensorflow的学习笔记

author:Damon

### Tensorflow2历史:

- 2019年3月，测试版发布
- 2019年10月，Tensorflow2.0发布
- 2020年1月，Tensorflow2.1发布

### 第一章：

#### Tensor(张量):

多维数组，阶：张量的维数

![image-20211228194804574](Tensorflow的学习笔记.assets/image-20211228194804574.png)

看方括号有几个，0个是0阶，n个是n阶

#### 数据类型：

![image-20211228194935742](Tensorflow的学习笔记.assets/image-20211228194935742.png)

#### 创建张量：

**tf.constant(张量内容，dtype=数据类型（可选）)**

![image-20211228195033140](Tensorflow的学习笔记.assets/image-20211228195033140.png)

![image-20211228195128255](Tensorflow的学习笔记.assets/image-20211228195128255.png)

最后一个，逗号隔开几个数字代表是几维向量

（2，）代表：1维，里面有两个元素

将numpy的数据类型转换为Tensor数据类型：

**tf. convert_to_tensor(数据名，dtype=数据类型(可选))**

![image-20211228195407274](Tensorflow的学习笔记.assets/image-20211228195407274.png)

![image-20211228195456339](Tensorflow的学习笔记.assets/image-20211228195456339.png)

![image-20211228195641288](Tensorflow的学习笔记.assets/image-20211228195641288.png)

![image-20211228195810681](Tensorflow的学习笔记.assets/image-20211228195810681.png)

常用函数

![image-20211228195927404](Tensorflow的学习笔记.assets/image-20211228195927404.png)

![image-20211228200054902](Tensorflow的学习笔记.assets/image-20211228200054902.png)

![image-20211228200303221](Tensorflow的学习笔记.assets/image-20211228200303221.png)

TensorFlow中的数学运算

![image-20211228201242837](Tensorflow的学习笔记.assets/image-20211228201242837.png)

![image-20211228201316606](Tensorflow的学习笔记.assets/image-20211228201316606.png)

![image-20211228201431081](Tensorflow的学习笔记.assets/image-20211228201431081.png)

![image-20211228201524126](Tensorflow的学习笔记.assets/image-20211228201524126.png)

![image-20211228201800950](Tensorflow的学习笔记.assets/image-20211228201800950.png)

![image-20211228201924492](Tensorflow的学习笔记.assets/image-20211228201924492.png)

![image-20211228201931794](Tensorflow的学习笔记.assets/image-20211228201931794.png)

![image-20211228202032035](Tensorflow的学习笔记.assets/image-20211228202032035.png)

![image-20211228202204618](Tensorflow的学习笔记.assets/image-20211228202204618.png)

![image-20211228202250926](Tensorflow的学习笔记.assets/image-20211228202250926.png)

![image-20211228202826693](Tensorflow的学习笔记.assets/image-20211228202826693.png)

![image-20211228203213563](Tensorflow的学习笔记.assets/image-20211228203213563.png)

![image-20211228203351162](Tensorflow的学习笔记.assets/image-20211228203351162.png)

![image-20211228203453626](Tensorflow的学习笔记.assets/image-20211228203453626.png)

**最大值的索引**



#### 鸢尾花分类实验

![image-20211228203848539](Tensorflow的学习笔记.assets/image-20211228203848539.png)



### 第二章

#### 预备知识

![image-20211228211734301](Tensorflow的学习笔记.assets/image-20211228211734301.png)

两个向量的最大值

![image-20211228212243886](Tensorflow的学习笔记.assets/image-20211228212243886.png)

![image-20211228212251547](Tensorflow的学习笔记.assets/image-20211228212251547.png)

![image-20211228212354746](Tensorflow的学习笔记.assets/image-20211228212354746.png)

![image-20211228213847531](Tensorflow的学习笔记.assets/image-20211228213847531.png)

![image-20211229011154123](Tensorflow的学习笔记.assets/image-20211229011154123.png)

![image-20211229011203949](Tensorflow的学习笔记.assets/image-20211229011203949.png)

![image-20211229011212707](Tensorflow的学习笔记.assets/image-20211229011212707.png)

![image-20211229011222241](Tensorflow的学习笔记.assets/image-20211229011222241.png)

![image-20211229011233607](Tensorflow的学习笔记.assets/image-20211229011233607.png)

![image-20211229011245481](Tensorflow的学习笔记.assets/image-20211229011245481.png)

![image-20211229011255622](Tensorflow的学习笔记.assets/image-20211229011255622.png)

![image-20211229011304483](Tensorflow的学习笔记.assets/image-20211229011304483.png)

![image-20211229011310857](Tensorflow的学习笔记.assets/image-20211229011310857.png)