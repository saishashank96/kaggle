# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:33:25 2019

@author: ons1kor
"""
count=0
count1=0
count2=0
count3=0
l=open(r"D:\Project\kaggle-master\results921.csv","r")
for k in l:
    k=k.split(",")
   
    if(int(k[1])!=int(k[2])):
        #print(k[0],k[1],k[2])
        if(int(k[2])==1):
            count=count+1
        else:
            count3=count3+1
    else:
        if(int(k[1])==int(k[2])):
            if(int(k[1])==1):
                count1=count1+1
            if(int(k[2])==0):
                count2=count2+1
print(count,count3,count1,count2)