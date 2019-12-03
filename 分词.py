# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 08:17:30 2019

@author: AntikoFang
"""

import jieba

s = '今天风好大的哦我的天，我真的真的真的好害怕！'
jieba.cut(s)  # 返回迭代器
jieba.lcut(s)

# 停用词
s1 = jieba.load_userdict(r'D:\PythonSpyder\NLP\jieba分词.txt')

jieba.lcut('今天风好大了啊，我好害怕的我')

#搜狗细胞词库
#https://pinyin.sougou.com/dict

#extract_tags 去除停用词

s = '今天风好大的哦我的天，我真的真的真的好害怕啊！'
newlist = [word for word in jieba.cut(s) if word not in ['的','啊']]
print(newlist)

jieba.analyse.set_stop_words()
import jieba.analyse as ana

ana.set_stop_words()

# 词性标注
import jieba.posseg as psg
sentence = '湖北经济学院大数据'
    #给出附加词性的标注 
psg.lcut(sentence) 

