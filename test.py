import pandas as pd
import numpy as np
from numpy import array
import csv
from sklearn.naive_bayes import GaussianNB
print("Welcome back shashank")


idd=[]
sur=[]
pclass=[]
#sex=[]
age=[]
a=0
b=0
c=0
d=0
X=[]
l=open("/home/saishashank/kaggle/train.csv")
for i in l:
	i=i.split(",")
	if(len(i[0])<8):
		print(i[5])
		if i[1]=="1":
			if i[5]=="male":
				a=a+1
			else:
				b=b+1
		else:
			if i[5]=="male":
				c=c+1
			else:
				d=d+1
		#if i[12] is true:
		#i[12]=i[12].strip("\n")
		'''if i[12]=="C":
			c=c+1
			#print("hi")
		if i[12]=="S":
			s=s+1
		if i[12]=="Q":
			q=q+1
		#pclass.append(int(i[2]))
#print(x)'''
print(a,b,c,d)
"""clf = GaussianNB()
#for i in range(len(idd)):
#	X.append([idd[i],pclass[i]])
#print(X)
#X=X.reshape(-1,1)
#np.reshape(-1,y)
#print("hi")
#print(len(X),len(y))
#print(X)
#X=np.array[[(x[i],y[i]) for i in range(len(x)) for j in range(len(y))] ]
clf.fit(X,sur)
X=[]
l=open("/home/saishashank/kaggle/test.csv")
for i in l:
	i=i.split(",")

	if(len(i[0])<8):
		#print(i[4])
		if i[4]=="male":
			i[4]="1"
		else:
			i[4]="0"
		if i[5]=="":
			i[5]="20"
		if i[9]=="":
			i[9]=20
		#print(i[0],i[1],i[4],i[5],i[6],i[7],i[9])
		X.append([int(i[0]),float(i[1]),float(i[4]),float(i[5]),float(i[6]),float(i[7]),float(i[9])])
		
		#X1.reshape(-1,1)
		#clf.predict([X1])
		#print("done")
l=open("/home/saishashank/kaggle/result.csv","w")
print(len(X))
i=0
for i in X:
	#l[0]=i[0]
	print(i)
	writer = csv.writer(l)
	c=clf.predict([i])

	for j in c:
		k=j
	print(i[0],k)
	writer.writerow([i[0],k])
	#print(clf.predict([i]))
"""
