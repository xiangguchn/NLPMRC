# 基于语料库的英语完形填空题目生成(corpus-based English colze question generation)

## 描述：
### 通过对语料进行学习，建造一个可以根据相关指标生成完形填空题目的生成器

## 方法：
### - 1：通过词与词之间的相似度生成考察词的候选集
### - 2：训练完形填空模型，通过模型找到空缺处不同词的概率分布，依据概率分布给出候选集

## 英语语料：
### CNN 新闻：https://cs.nyu.edu/~kcho/DMQA/

## 1:将story文件中的文本转到txt文件中(story_to_txt.py)
### 删除与文章不相关信息如："(CNN) --"等
### 将所有段落拼接为一个字符串
### 将所有story存为一个列表，保存到cnnstories.txt中

## 2：分词并建立词典(vocab.py)：
### 利用nltk对stories分词，得到包含单词及index的vocab.txt以及包含单词及频率的vocab_frequency.txt
###  词典中单词的词频可以作为衡量单词难易程度及重要程度的标准
