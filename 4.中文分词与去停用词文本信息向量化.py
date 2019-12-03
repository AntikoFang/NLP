# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 08:15:34 2019

@author: chensiyi
"""

'''jieab库'''
#jieba.cut()是迭代器
#jieba.lcut()是列表
#jieba.add_word()、jieba.del_word()
import jieba
s = '武汉的风好像会说话，他刚刚对我说，我要你死'
jieba.cut(s) #迭代器,循环输出结果
jieba.lcut(s) #精确模式
jieba.lcut(s, cut_all=True) #全模式,所有可能的词都显示
jieba.lcut_for_search(s) #搜索引擎模式

#自定义词典
#load_userdict(file_name)一行一词,词、词频、词性,用空格隔开
jieba.load_userdict(r'D:\PythonSpyder\NLP\jieba分词.txt')
#搜狗细胞词库https://pinyin.sogou.com/dict/
#去除停用词(一些不重要的词,不携带有效信息) 用extrat_tags去停用词同时分词
#新列表 = []
l = jieba.lcut(s)
l = jieba.cut(s)
newlist = [i for i in l if i not in ['的', '他', '，']]
print(newlist)

import jieba.analyse as ana
    # 设置停用词
ana.set_stop_words(r'D:\PythonSpyder\NLP\jieba分词.txt')  
s = '武汉的风好像会说话呀，他刚刚对我说呢，我要你死哦'       
    # 分词与停用词同时进行
ana.extract_tags(s)                                      

#词性标注
import jieba.posseg as psg
s = '武汉的风好像会说话呀，他刚刚对我说呢，我要你死哦'
psg.lcut(s)











































