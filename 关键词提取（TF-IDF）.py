# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 08:16:57 2019

@author: AntikoFang
"""

"""

TF-IDF
词在这篇文章出现的频率，以及在语料库出现的频率

TF：Term Frequency 衡量一个term在文档中出现的次数
TF(t) = t出现在文档中的次数/文档中出现term次数最多的

逆文档频率IDF：Inverse Docment Frequency
IDF(t) = log(语料库中文档总数)/(含有term的文档总数+1) --防止分母为0的情况

TF * IDF(值相乘) = TF-IDF
乘积越大，词越重要
与一个词在文档出现次数成正比
与该词在整个语料库中出现次数成反比

TF-IDF实现
jiaba
NLTK
gensim


jiaba.analyse.extract_tags 分词后返回TF/IDF权重最大的a个词
"""
import jieba
import jieba.analyse

doc = """百丽咬着筷子头，不以为然地说。
 　　“哟，说得好像当时你没参与似的。”戈壁笑，笑得倾国倾城，眼睛却盯着洛枳。
 　　“我……就是觉得把你的哥们都晾着不太好。”
 　　“其实是你怕被我们晾着吧。”
 　　“你没完了是不是！”百丽嘴里还叼着筷子头，脸迅速涨红了，斜眼睛瞪着戈壁。眼看两人又要杠起来，洛枳楞了一下，开始认真地履行她坐在这里的责任，“百丽这是你买的？食堂做的麻辣鸭脖子好吃吗？”
 　　百丽转过来，说，“就剩两块了，你吃吧。我去买杯可乐，你要不要？”
 　　洛枳还没说话她就直接冲出去了。
 　　“这话题岔得可不高明。”戈壁冷笑。
 　　洛枳低头，咬了一口鸭脖子肉最肥厚的内侧弯，不笑也不说话。
 　　“前阵子听说你也感冒了？”她听出戈壁特意强调的那个“也”字。
 　　“哦。”
 　　“现在好了？”
 　　废话真多。她眉头微蹙，抬起头看他。
 　　“你真是挺混蛋的。”她的语气好像在描述鸭脖子太咸了一样平静。
 　　戈壁还没来得及反应，就听到百丽在远处喊，来接我一下，打了三杯拿不住。
 　　他没有动，洛枳放下筷子去接过两杯可乐。百丽径直把手里的一杯先放到了戈壁的前面。
 　　之后的江百丽像是害怕冷场一样不停地讲话，洛枳随着她胡乱地扯几句有的没的，戈壁还是不说话，较劲一般盯着喝粥的洛枳不放。
 　　洛枳吃得很快，没有让他们两个等太久，三个人一起站起来收餐盘，百丽走到前面先送走了一些。
 　　“我这是跟你第二次讲话吧，咱俩没仇吧？干嘛老是拿话刺儿我？”戈壁半眯着眼睛，怒火中也有一点点做作。洛枳明明白白地把目光迎上去看他驾轻就熟的笑容和姿态。
 　　她把到嘴边的话都咽下去。尽管只是第二次跟他讲话，但她知道，戈壁这种人，最喜欢女生自以为伶牙俐齿地跟他玩个性斗来斗去，所以忍一时风平浪静。
 　　“我没听说百丽和你是闺蜜啊？你倒挺护着她。”对方不依不饶。
 　　我倒听说你的确不识好歹。洛枳在心里默念了一句，把餐盘往台子上一推，拿出面巾纸擦擦手，冲百丽喊，“喂，我要去趟超市，先走了。”
 她忘记系紧外套，推门的瞬间灌了满怀凉风。走了几步，朝他们离开的方向看过去，百丽没穿外套，挽着戈壁的背影在秋风中显得很单薄。洛枳有些悲哀，她印象中仅有几次看到两个人在一起的时候，他们都不牵手，一直是江百丽挽着戈壁，紧紧地。
"""

jieba.analyse.extract_tags(doc,withWeight= True)

jieba.analyse.set_idf_path('D:\PythonSpyder\橘生淮南词云图\橘生淮南.txt')

# 新建 TF-IDF模型实例
jieba.analyse.TFIDF(idf_path = None)


# TF-IDF的sklearn实现
'''
导入文件
分词去停用词
用空格连接
导包
转换为词频矩阵
算TF-IDF
'''
import pandas as pd
diao = pd.read_csv(r'C:\Users\Administrator\Documents\Tencent Files\1521131720\FileRecv\射雕_chapter.csv',
                   engine = 'python',
                   encoding = 'utf-8',
                   index_col = 0)
diao.head()
# 停用词
s1 = jieba.load_userdict(r'D:\PythonSpyder\NLP\jieba分词.txt')
jieba.lcut(diao)

from sklearn.feature_extraction.text import TfidfTransformer
diao_tfidf = TfidfTransformer()
diao_tfidf.todense() #转换为矩阵

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()

# 每列对应的词
vectorizer.get_feature
#词条字典
vectorizer.vocabulary_





















