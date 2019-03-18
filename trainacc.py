# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:33:25 2019

@author: ons1kor
"""
count=0
l=open("/home/saishashank/kaggle/result25.csv","r")
for k in l:
    k=k.split(",")
    print(type(k[1]))
    if(int(k[1])!=int(k[2])):
        print(k[1],k[2])
        count=count+1
print(count)