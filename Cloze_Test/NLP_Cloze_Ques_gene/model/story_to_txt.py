# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 08:11:15 2020

@author: xiangguchn
"""
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))


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
        
        if ii%1000 == 0:
            print('one thousand stories are finished')
        
        # add stories to one list
        stories.append(story)
    
    # save all stories to txt file
    stories_path='{}\\dataset\\cnnstories.txt'.format(BASE_DIR)    
    save_stories(stories, stories_path)
    
    
# save stories to stoies.txt file
def save_stories(stories, stories_path):
    
    with open(stories_path, 'w', encoding='utf-8') as f:
        for story in stories:
            f.write('%s\n' % story.strip())
    print('save sentence:%s' % stories_path)



if __name__ == '__main__':
    main()




