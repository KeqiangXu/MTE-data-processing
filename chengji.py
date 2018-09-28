# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 11:08:07 2018

@author: X
"""
import numpy as np
import pandas as pd


#————————————————————————读取txt 存储为xlsx————————————————————————————
#————————————————————————分步解析——————————————————————————————————————

file = open('e:/learn python/MTE/report.txt', 'r', encoding = 'UTF-8')
lines = file.read().splitlines()  #按行读取txt文件(并去掉最后的\n)
file.close()
def df_pro():
    df = pd.DataFrame(columns = (lines[0].split(' '))) #创建新的dataframe
    for i in range(len(lines)-1): 
        df.loc[i] = (lines[i+1].split(' ')) #在DataFrame中添加新的一行
    for string in df.columns:
        if string == '姓名':
            df = df.astype({string:'str'})
        else:
            df = df.astype({string:'int'})  #数据类型转换
    studentsum =df.sum(axis = 1) #计算各个学生的总成绩并添加新的一列
    studentmean = df.mean(axis = 1) #计算各个学生的平均成绩并添加新的一列
    df['学生总成绩'] = studentsum
    df['学生平均成绩'] = studentmean
    #df.sort_values(columns = ['a'],axis = 0,ascending = True) #升序排列
    df = df.sort_values('学生平均成绩',axis = 0,ascending = False) #降序排列
    subjectmean = []
    for string in df.columns:
        if string == '姓名':
            subjectmean = ['各科平均成绩']
        else:
            subjectmean.append(df[string].mean())
    df.loc[len(lines)] = (subjectmean)
    df = df.reset_index() #重置索引
    del df['index'] #删掉旧的索引列
    df[df.iloc[:,1:10]<60] = np.nan #将第1列至第10列中小于60的替换为nan
    df = df.fillna('不及格') #将表中所有nan替换为 不及格
    rank = [] #建立排名
    for i in range(len(df)):
        rank.append(i+1)
    df['名次'] = rank
    r = df.pop('名次') #移动列
    df.insert(1,'名次',r) 
    return(df)

df = df_pro()
df.to_excel('E:/learn python/MTE/data_pro.xlsx', encoding='utf-8', index=False) #保存为xlsx


'''
pandas数据分析基础语句
df.sum() #对列进行求和
df.sum(axis=1) #对行进行求和
df.mean(axis=1, skipna=False)
axis为所选择的轴
skipna排除缺失值，默认为True
'''




