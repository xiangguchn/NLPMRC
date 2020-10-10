# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:52:16 2020

@author: xiangguchn
"""

# get project root path
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))

# import modules needed
import nltk
from collections import defaultdict


def story_token(stories_path):
    
    with open(stories_path, 'r', encoding='utf-8') as stories:
        words = []
        for story in stories:            
            words += nltk.word_tokenize(story)
    
    return words

                
def build_vocab(items, sort=True, min_count=0, lower=False):

    result = []
    if sort:
        dic = defaultdict(int)
        for item in items:
            for i in item.split(' '):
                i = i.strip()
                if not i: continue
                i = i if not lower else item.lower()
                dic[i] += 1
        
        # sort by word frequency in vocab
        dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        
        for i, item in enumerate(dic):
            # print(i, item)
            key = item[0]
            if min_count and min_count>item[1]:
                continue
            # print('-----------------', key)
            result.append(key)
    else:
        for i, item in enumerate(items):
            item = item if not lower else item.lower()
            result.append(item)
    
    # build vocab and reverse vocab
    vocab_frequency = dic
    vocab = [ (item[0], index) for index, item in enumerate(dic)]
    vocab_reverse = [(index, item[0]) for index, item in enumerate(dic)]
    
    return  vocab, vocab_reverse, vocab_frequency


def save_word_dict(vocab, vocab_path='{}/datasets/vocab.txt'.format(BASE_DIR)):
    with open(vocab_path, 'w', encoding='utf-8') as f:
        for line in vocab:
            w, i = line
            f.write('%s\t%d\n'%(w,i))


if __name__ == '__main__':
    
    # segerate stories to words with nltk
    stories_path = '{}\\dataset\\cnnstories.txt'.format(BASE_DIR)    
    words = story_token(stories_path)    

    # build vocab and save them
    vocab, vocab_reverse, vocab_frequency = build_vocab(words)  
    save_word_dict(vocab, '{}/dataset/vocab.txt'.format(BASE_DIR))
    save_word_dict(vocab_frequency, '{}/dataset/vocab_frequency.txt'.format(BASE_DIR))






