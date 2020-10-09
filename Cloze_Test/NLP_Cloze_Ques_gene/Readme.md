# 基于语料库的英语完形填空题目生成(corpus-based English colze question generation)

## 描述：
### 通过对语料进行学习，建造一个可以根据相关指标生成完形填空题目的生成器，词典中单词的词频可以作为衡量单词难易程度及重要程度的标准

## 方法：
### 1：通过词与词之间的相似度生成考察词的候选集
### 2：训练完形填空模型，通过模型找到空缺处不同词的概率分布，依据概率分布给出候选集

## 英语语料：
### CNN 新闻：https://cs.nyu.edu/~kcho/DMQA/

## 1: 将story文件中的文本转到txt文件中(story_to_txt.py)
### 删除与文章不相关信息如："(CNN) --"等
### 将所有段落拼接为一个字符串
### 将所有story存为一个列表，保存到cnnstories.txt中

## 2: 分词并建立词典(vocab.py)：
### 利用nltk对stories分词，得到包含单词及index的vocab.txt以及包含单词及频率的vocab_frequency.txt

## 3: 训练词向量(word2vec.py)
### 以cnnstories.txt作为语料，训练词向量得到w2v_part.bin

## 4: 建立英语常考词汇表
### 在网上找到一些英语经常考查的词汇，存在gaokao_clozetest_words.txt

## 5: 确定常考词汇的相似词及包含常考词汇的文章（gaokaowords_similarities.py)
### 通过词向量计算词典中词语与高考常考词语之间的相似度，为每个单词找到四个相似度最大的词作为完形填空的候选集
### 寻找包含某个单词的story，
### 将单词，单词相似词以及所有包含单词story的index存在一起，保存为gaokaowordssimistoryindex.csv

## 6: 建立完形填空题目生成器（examination_question_generation.py)
### 给定想要考查的词汇，寻找包含所有这些词汇的story。（目前只使用了10000个stories训练，如果随机给定10个考查词汇，很难找到完全包含这些词的story）
### 给了100个考查词汇，最多的文章包含其中19个词，随机选取前100篇文章中的一篇，并将文章，考查词汇以及考查词汇的相似词存入exam/index.txt文件中
