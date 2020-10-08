# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 22:44:25 2020

@author: xiangguchn
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))

import pandas as pd

def main():
    
    # get filenames under given filePath
    filePath = '{}\\dataset\\cnnstories\\'.format(BASE_DIR)        
    filenames = os.listdir(filePath)
    
    # get stories from all story files
    stories = []
    ii = 0
    for file in filenames:
        story = ''
        ii += 1
        with open(filePath+file, 'r', encoding='utf-8') as lines:
            i = 0
            for line in lines:
                i += 1
                # line with only \n is not useful
                if line=='\n':
                    # print('--')
                    continue
                # line start wiht '@' and end with 'contributed to this report.' means story end
                if line[0]=='@' or line[-27:]=='contributed to this report.':
                    break
                if '(CNN) --' in line:
                    line = line[line.index('(CNN) --')+9:]
                # print(line[:-2])
                # add all lines to one
                story += line[:-1] + ' '
        
        # add stories to one list
        stories.append(story)
        
        if ii == 10000:
            print('Ten thousand stories are finished')
            break
    
    # save all stories to txt file
    stories_path='{}\\dataset\\cnnstories_part.txt'.format(BASE_DIR)    
    save_stories(stories, stories_path)
    
    stories_csv_path = '{}\\dataset\\cnnstories_part.csv'.format(BASE_DIR) 
    save_stories_csv(stories, stories_csv_path)
    
    
# save stories to stoies.txt file
def save_stories(stories, stories_path):
    
    with open(stories_path, 'w', encoding='utf-8') as f:
        for story in stories:
            f.write('%s\n' % story.strip())
    print('save sentence:%s' % stories_path)


# save stories to cnnstories_part.csv with index
def save_stories_csv(stories, stories_csv_path):
    
    ds = [(item[0], item[1]) for item in enumerate(stories)]
    dataframe = pd.DataFrame(ds)
    dataframe.to_csv(stories_csv_path, index=False, sep=',')
    
    
    
if __name__ == '__main__':
    main()
