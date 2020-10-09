# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 00:09:56 2020

@author: xiangguchn
"""

# get project root path
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))

import numpy as np
import pandas as pd
from gensim.models.keyedvectors import KeyedVectors

# gaokao words
def gaokao_words(gaokaowords_path):
    
    gaokaowords = []
    with open(gaokaowords_path, 'r', encoding='utf-8') as f:
        for word in f:
            if word[-1:] == '\n':
                gaokaowords.append(word[:-1])
            else:
                gaokaowords.append(word)
    
    return gaokaowords


def vocab_words(vocab_part_path):
    
    vocabwords = []
    with open(vocab_part_path, 'r', encoding='utf-8') as f:
        for word in f:
            word = word[:word.index('\t')]
            vocabwords.append(word)
    
    return vocabwords



def words_similiraty(gaokaowords, vocabwords, word2vec_part):
    
    wordssimiliraty = []
    nv = len(vocabwords)
    for word in gaokaowords:
        
        sims = [0 for _ in range(nv)]
        
        for i in range(nv):
            try:
                sims[i] = word2vec_part.wv.similarity(word, vocabwords[i])
            except:
                continue
            
        ind = np.argsort(sims)[-4:]
        
        indw = [vocabwords[i] for i in ind]
        # for i in ind:
        #     print(sims[i])
        #     ii = vocabwords[i].index('\t')
        #     indw.append(vocabwords[i][:ii])
        
        print(word, "'s similarities is ", indw)
        
        wordssimiliraty.append([word, indw])
        
    return wordssimiliraty


    

def storyindex_with_certain_word(gaokaowords, cnnstoriespart):
    
    wordstoryindex = []
    ns = len(cnnstoriespart)
    for i in range(len(gaokaowords)):
        
        word = gaokaowords[i]
        ind = []
        
        for j in range(ns):
            try:
                if word in cnnstoriespart['1'][j]:
                    ind.append(j)
            except:
                continue
            
        wordstoryindex.append([word, ind])

    return wordstoryindex
     


if __name__ == '__main__':
    
    # get word2vec 
    w2v_bin_path = '{}/dataset/w2v_part.bin'.format(BASE_DIR)
    word2vec_part = KeyedVectors.load_word2vec_format(w2v_bin_path, binary=False)
    
    # get gaokao words list
    gaokaowords_path = '{}/dataset/gaokao_clozetest_words.txt'.format(BASE_DIR)
    gaokaowords = gaokao_words(gaokaowords_path)
    
    # get vocab words
    vocab_part_path = '{}/dataset/vocab_part.txt'.format(BASE_DIR)
    vocabwords = vocab_words(vocab_part_path)
    
    # get gaokao words' similiarity vocabs
    wordssimiliraty = words_similiraty(gaokaowords, vocabwords, word2vec_part)
    
    
    # get cnnstories_part
    cnnstories_part_path = '{}/dataset/cnnstories_part.csv'.format(BASE_DIR)
    cnnstoriespart = pd.read_csv(cnnstories_part_path, encoding='utf-8')
    
    # get stories indexs with given gaokaowords
    wordstoryindex = storyindex_with_certain_word(gaokaowords, cnnstoriespart)
    
    
    # combine gaokao words' similiarity words and cnnstories with given words
    gaokaowordsimistoryindex = [[wordssimiliraty[i][0], wordssimiliraty[i][1], wordstoryindex[i][1]] for i in range(len(wordssimiliraty))]
    
    
    # save result
    gaokaowordsimistoryindex_path = '{}/dataset/gaokaowordsimistoryindex_path.csv'.format(BASE_DIR)
    gkwordssimisi = pd.DataFrame(gaokaowordsimistoryindex)
    gkwordssimisi.to_csv(gaokaowordsimistoryindex_path, encoding='utf-8')





