# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:46:44 2020

@author: xiangguchn
"""


# get project root path
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))

# load modules needed
from gensim.models import Word2Vec

# build word2vec
def build(sentence_path='{}/dataset/cnnstories_part.txt'.format(BASE_DIR),
          w2v_bin_path = '{}/dataset/w2v_part.bin'.format(BASE_DIR)):
    
    # used to test code
    sentence_path='{}/dataset/cnnstories_part.txt'.format(BASE_DIR)
    w2v_bin_path = '{}/dataset/w2v_part.bin'.format(BASE_DIR)
    
    
    # train word2vec
    print('train w2v part model ...')
    # sg=1 means skip-gram
    w2v = Word2Vec(corpus_file=sentence_path, size=256, window=5, sg=1, min_count=5)


    # save word2vec result
    w2v.wv.save_word2vec_format(w2v_bin_path, binary=False)
    print('save %s ok.' % w2v_bin_path)
    
    
    # test word2vec training result
    sim = w2v.wv.similarity('better','good')
    print('similarity score between good and better is ', sim)
    
        
if __name__ == '__main__':
        
    # build word2vec and save them
    build(sentence_path='{}/dataset/cnnstories_part.txt'.format(BASE_DIR),
          w2v_bin_path = '{}/dataset/w2v_part.bin'.format(BASE_DIR))
