# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 22:48:32 2020

@author: xiangguchn
"""

# get project root path
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))

import random
import pandas as pd

def gaokao_words(gaokaowords_path):
    
    gaokaowords = []
    with open(gaokaowords_path, 'r', encoding='utf-8') as f:
        for word in f:
            if word[-1:] == '\n':
                gaokaowords.append(word[:-1])
            else:
                gaokaowords.append(word)
    
    return gaokaowords



def exam_ques_gen_simi(wordswanted, cnnstories_part_index, gkwordssimisi):
    
    words = [gkwordssimisi['0'][i] for i in range(len(gkwordssimisi))]
    
    storyindexs = []
    for word in wordswanted:
        index = words.index(word)
        si = gkwordssimisi['2'][index][1:-1].split(', ')
        sii = [int(i) for i in si if len(i)!=0]
        storyindexs += sii
    
    # random choice one story as examination question
    st = pd.value_counts(storyindexs)    
    storyindex = random.choice(st.index[:100])
    print('index of cnn story used of examination is', storyindex)
    
    # get gaokao words in chosed story
    wordssimi = []
    strs = ' ' + str(storyindex) + ','
    for i in range(len(gkwordssimisi)):
        if strs in gkwordssimisi['2'].values[i]:
            print(gkwordssimisi['0'].values[i], "'s similiraties are: ", gkwordssimisi['1'].values[i])
            wordssimi.append([gkwordssimisi['0'].values[i], gkwordssimisi['1'].values[i]])
    
    return storyindex, wordssimi



def exam_ques_gen_pred():
    
    # next target
    pass


def save_exam(exam_ques_gened_path, cnnstory, wordssimi):
    
    with open(exam_ques_gened_path, 'w', encoding='utf-8') as f:
        # save story
        f.write('%s\n'%cnnstory)
        # save gaokaowords and its similarities
        for line in wordssimi:
            # print(line)
            f.write('%s\n'%str(line))



if __name__ == '__main__':
    
    # words one want to be contant in one examination question generated
    gaokaowords_path = '{}/dataset/gaokao_clozetest_words.txt'.format(BASE_DIR)
    gaokaowords = gaokao_words(gaokaowords_path)
    # wordswanted = ['immediate', 'clear', 'cautious', 'vivid', 'exactly', 
    #                'fortunately', 'surprisingly', 'hardly', 'instead', 'properly']
    # wordswanted = random.sample(gaokaowords, 10)
    wordswanted = random.sample(gaokaowords, 100)
    
    # cnnstories with index
    cnnstories_part_path = '{}/dataset/cnnstories_part.csv'.format(BASE_DIR)
    cnnstories_part_index = pd.read_csv(cnnstories_part_path, encoding='utf-8')
    
    # gaokaowords with similraties and story index
    gaokaowordsimistoryindex_path = '{}/dataset/gaokaowordsimistoryindex.csv'.format(BASE_DIR)
    gkwordssimisi = pd.read_csv(gaokaowordsimistoryindex_path, encoding='utf-8')
    
    
    # generate examination question
    mode = 'similarity'
    if mode == 'similarity':
        storyindex, wordssimi = exam_ques_gen_simi(wordswanted, cnnstories_part_index, gkwordssimisi)
    elif mode == 'prediction':        
        storyindex, wordssimi = exam_ques_gen_pred(wordswanted, cnnstories_part_index, gkwordssimisi)

    
    # save result
    exam_ques_gened_path = '{}/dataset/exams/'.format(BASE_DIR)+str(storyindex)+'.txt'
    cnnstory = cnnstories_part_index['1'][storyindex]
    save_exam(exam_ques_gened_path, cnnstory, wordssimi)
    
    



