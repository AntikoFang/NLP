# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:22:00 2019

@author: Administrator
"""

import logging
from gensim.models import word2vec
 
def main():
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO)
    sentences = word2vec.LineSentence(r"E:\Word2Vec-Wiki\zhwiki\data\wiki_corpus")		#注意替换成你的路径
    model = word2vec.Word2Vec(sentences,size=250)	# size默认是100-300，根据你的语料大小进行增加，效果看你的需求
    #保存模型
    model.save(r"E:\Word2Vec-Wiki\WikiModel-MyModel\wiki_corpus.model")		# 我的代码是保存为zhwiki_news.word2vec，需要你自己改下
	
if __name__ == '__main__':
	main()
	
