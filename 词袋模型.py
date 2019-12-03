# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 09:14:19 2019

@author: AntikoFang
"""
# 词袋模型介绍
'''
词袋模型 BOW  （bag of word）
    可以不考虑词频，减少模型复杂度
    常见于短文本分析
优点：
    1. 解决了分类器不好处理离散数据的问题
    2. 一定程度上起到了扩充特征的作用
缺点：
    1. 词之间的顺序不存在了
    2. 假设词与词是相互独立的
    3. 得到的特征是离散稀疏的

eg.
大鱼吃小鱼也吃虾米 --> [大鱼,吃,小鱼,也,虾米] --> [1,2,1,1,1]
小鱼吃虾米        -->  [小鱼,吃,虾米]        --> [0,1,1,0,1]
'''
# 词袋模型实现
'''
sklearn 来实现
    1. 文档信息向量化 （CountVectorizer类）
'''

#统计词频
from sklearn.feature_extraction.text import CountVectorizer
    # 实例化
countvec = CountVectorizer(min_df = 2) # 出现两个以上文档出现的才保留

x = countvec.fit_transform(['湖北 经济 学院 大 数据','数据 科学 技术部 经济']) # 文档之间的词用空格连接
type(x)  #scipy.sparse.csr.csr_matrix    文本向量化了

x.todense() #将稀疏矩阵直接转换为标准格式矩阵

countvec.get_feature_names() # 看是哪些词 词汇列表，实际上就是获取没个列对应的词条


countvec = CountVectorizer()
x = countvec.fit_transform(['湖北 经济 学院 大 数据','数据 科学 技术部 经济'])
x.todense()
countvec.get_feature_names()


countvec.vocabulary_  # 排序 统计词频
'''
# gensim 实现
    1. 建立字典
'''
#1.建立字典
import gensim
from gensim.corpora import Dictionary

texts = [["湖北",'武汉','hello','world','welcome'],['hello','welcome','Hello','world','大数据']]
dct = Dictionary(texts)

    '''
    token2id : dict of (str,int) - token -> tokenID
    id2token : dict of (int,str) 
    dfs : dict of (int,int)
    '''
dct.token2id #查看词汇编码  0 1 2 3 4 5 6
    
dct.dfs      #查看每个词汇出现次数

dct.num_pos  #查看处理过程的词汇数量
dct.num_nnz  #与num_pos 类似

dct.add_documents([['cat','bird','cute'],['动物','植物','panda']])  #增加词条
dct.token2id #查看词汇编码  0 1 2 3 4 5 6

dct.doc2idx(['this','cat','is','cute']) #查询词汇在字典中的编码  没有的就饿返回-1

    #准换为BOW稀疏向量
dct.doc2bow(['this','is','a','cute','cat'],  #8(cute) 和 9(cat) 出现了 1次
            return_missing=True,  #词库没有的词
            allow_update=True     #把词库没有的词加入词库 是否直接更新所用字典
            )
dct.token2id
















