l=open("/home/saishashank/kaggle/result2.csv","r")
m=open("/home/saishashank/kaggle/result5.csv","r")


#i=i.split(",")
#j=j.split(",")
for k in range(418):
	i=l.readline()
	#print(i)
	i=i.split(",")
	#print(i[0])
	j=m.readline()
	j=j.split(",")
	if i[1]!=j[1]:
		print(i[0],i[1],j[1])