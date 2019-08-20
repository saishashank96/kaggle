# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:21:39 2019

@author: ons1kor
"""

import csv
from sklearn import svm
from sklearn.ensemble import GradientBoostingClassifier
idd=[]
sur=[]
pclass=[]
#sex=[]
age=[]

P=[]
Q=[]
X=[]
l=open(r"C:\Users\ons1kor\Automation\Project\Kaggle\Project-housing\train.csv")
Mszone={"A":1,"C (all)":2,"FV":3,"I":4,"RH":5,"RL":6,"RP":7,"RM":8}
stnall={"Grvl":1,"Pave":2,"NA":3}
Lotsh={"Reg":1,"IR1":2,"IR2":3,"IR3":4}
Landcon={"Lvl":1,"Bnk":2,"HLS":3,"Low":4}
Util={"AllPub":1,"NoSewr":2,"NoSeWa":3,"ELO":4}
LotConfig={"Inside":1,"Corner":2,"CulDSac":3,"FR2":4,"FR3":5}
Neigh={"Blmngtn":1,
"Blueste":2,
"BrDale":3,
"BrkSide":4,
"ClearCr":5,
"CollgCr":6,
"Crawfor":7,
"Edwards":8,
"Gilbert":9,
"Names":10,
"NoRidge":11,
"NPkVill":12,
"NridgHt":13,
"NWAmes":14,
"OldTown":15,
"SWISU":16,
"Sawyer":17,
"SawyerW":18,
"Somerst":19,
"StoneBr":20,
"Timber":21,
"Veenker":22
}



for i in l:
    i=i.split(",")
    #print(i)
    if len(i[1])<5:
        
    