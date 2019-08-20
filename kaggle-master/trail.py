# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:11:46 2019

@author: ons1kor
"""
import re
p="keep calm and clean data"
#first=re.match("\w*(?= )",p)
#rest=re.findall("(?<= )\w*",p)
rest2=re.findall("\A\w*(?= )|(?<= )\w*",p)
Count=len(rest2)
string=rest2[Count-1]
for i in range(2,Count+1):
    string=string+" "+rest2[Count-i]   
print(string)
#string=""
#string=[rest2[p-i] for i in range(1,p+1)]
#print(string)

#print([rest]+first.group())

