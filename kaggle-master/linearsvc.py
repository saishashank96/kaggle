# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:09:08 2019

@author: ons1kor
"""
import csv
from sklearn import svm
from sklearn.ensemble import BaggingClassifier
#import matplotlib.pyplot as plt
#import seaborn as sns
idd=[]
sur=[]
pclass=[]
#sex=[]
age=[]

X=[]
#P=[]
l=open(r"C:\Users\ons1kor\Automation\Project\other\Kaggle\kaggle-master\train.csv")
for i in l:
	i=i.split(",")

	if(len(i[0])<8):
		i[12]=i[12].strip("\n")
		if i[12]=="C":
			i[12]=0
			#print("hi")
		if i[12]=="S":
			i[12]=1
		if i[12]=="Q":
			i[12]=2
		else:
			i[12]=0
		if i[5]=="male":
			i[5]=1
		else:
			i[5]=0
		age=i[4].split(".")
		if i[6]=="":
			#print(i)
			if age[0]==" Mr":
			    #print(i[0])
			    i[6]="35"
			if age[0]==" Mrs":
			    i[6]="40"
			if age[0]==" Miss":
			    i[6]="12"
			else:
			    i[6]="4"	
		#P.append([float(i[6])])
		X.append([int(i[0]),float(i[2]),float(i[5]),float(i[6]),float(i[7]),float(i[8]),float(i[10]),float(i[12])])
		sur.append(int(i[1]))
		#pclass.append(int(i[2]))
#print(x)
clf = svm.SVC(kernel='linear', C =1 )
#for i in range(len(idd)):
#	X.append([idd[i],pclass[i]])
#print(X)
#X=X.reshape(-1,1)
#np.reshape(-1,y)
#print("hi")
#print(len(X),len(y))
#print(X)
#X=np.array[[(x[i],y[i]) for i in range(len(x)) for j in range(len(y))] ]

Q=[]
#plt.scatter(P,sur)
#clf.fit(X,sur)
m=BaggingClassifier(base_estimator=clf,n_estimators=10,max_samples=0.5)
m.fit(X,sur)
X=[]
l=open(r"D:\Project\kaggle-master\test.csv")
for i in l:
	i=i.split(",")

	if(len(i[0])<8):
		#print(i[4])
		i[11]=i[11].strip("\n")
		if i[11]=="C":
			i[11]=0
			#print("hi")
		if i[11]=="S":
			i[11]=1
		if i[11]=="Q":
			i[11]=2
		else:
			i[11]=0

		if i[4]=="male":
			i[4]="1"
			#print(i[4])
		else:
			i[4]="0"
		age=i[3].split(".")            
		if i[5]=="":
			#print(i)
			if age[0]==" Mr":
			    #print(i[0])
			    i[5]="35"
			if age[0]==" Mrs":
			    i[5]="40"
			if age[0]==" Miss":
			    i[5]="12"
			else:
			    i[5]="4"
		if i[9]=="":
			i[9]=20
		#print(i[0],i[1],i[4],i[5],i[6],i[7],i[9])
		Q.append([int(i[0])])
		X.append([int(i[0]),float(i[1]),float(i[4]),float(i[5]),float(i[6]),float(i[7]),float(i[9]),float(i[11])])
		
		#X1.reshape(-1,1)
		#clf.predict([X1])
		#print("done")

l=open(r"D:\Project\kaggle-master\result602.csv","w", newline='')
#print(len(X))
i=0
#C=[]
b=0
n=0
#m=0
writer = csv.writer(l)
writer.writerow(["PassengerId","Survived"])
for i in X:
	#l[0]=i[0]
	#print(i)
	
	c=m.predict([i])

	for j in c:
		k=j
	#print(i[0],k)
	writer.writerow([i[0],k])
	#C.append(c)
#	b=b+1
	#print(clf.predict([i]))
l.close()
