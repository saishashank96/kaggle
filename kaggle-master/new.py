# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:47:14 2019

@author: ONS1KOR
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn import svm
from sklearn.neural_network import MLPClassifier
import csv
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
#import xgboost
from xgboost import XGBClassifier

train=pd.read_csv(r"C:\Users\ons1kor\Automation\Project\other\Kaggle\kaggle-master\train.csv")
test=pd.read_csv(r"C:\Users\ons1kor\Automation\Project\other\Kaggle\kaggle-master\test.csv")

print("train data shape",train.shape)
print("test data shape",test.shape)

print(train.Survived.describe())
print(train.Survived.skew())

#target=np.log(train.Survived)
#print(target.skew())

numeric_features = train.select_dtypes(include=[np.number])
corr=numeric_features.corr()
print(corr['Survived'].sort_values(ascending=False))


nulls = pd.DataFrame(train.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
#nulls
print(nulls)

categoricals = train.select_dtypes(exclude=[np.number])
#categoricals.describe()
print(categoricals.describe())


train['enc_Sex'] = pd.get_dummies(train.Sex, drop_first=True)
test['enc_Sex'] = pd.get_dummies(test.Sex, drop_first=True)

print ('Encoded: \n')


train['Embarked']=train['Embarked'].astype('category')


train['enc_Embarked']=train['Embarked'].cat.codes
print (train.enc_Embarked.value_counts())

test['Embarked']=test['Embarked'].astype('category')


test['enc_Embarked']=test['Embarked'].cat.codes
#print (test.enc_Embarked.value_counts())


categoricals = train.select_dtypes(exclude=[np.number])
#categoricals.describe()
#print(categoricals.describe())






numeric_features = train.select_dtypes(include=[np.number])
corr=numeric_features.corr()
#print(numeric_features.describe())
#print(corr['Survived'].sort_values(ascending=False))

# =============================================================================
# np.any(np.isnan(train.Fare))
# if np.any(np.isnan(train.Fare)):
#     print("abc")
# 
# =============================================================================
# =============================================================================
# train['Fare']=np.nan_to_num(train.Fare)
# np.any(np.isnan(train.Fare))
# np.any(np.isnan(train.PassengerId))
# np.any(np.isnan(train.PassengerId))
# =============================================================================
#print(train['Fare'])

data = train.select_dtypes(include=[np.number]).interpolate().dropna()



# sum(data.isnull().sum() != 0)
print(sum(data.isnull().sum() != 0))







train['Fare']=train['Fare'].astype(np.float64)






y=train.Survived
X=data.drop(['Survived','PassengerId'],axis=1)
#print(test.describe())
X1,X2,Y1,Y2=train_test_split(X,y,random_state=42,test_size=.33)
#np.where(np.isnan(X1))
#clf1=svm.SVC(kernel='linear', C =1)
clf=XGBClassifier(
 learning_rate =0.01,
 #booster='gblinear',
 n_estimators=5000,
 max_depth=4,
 min_child_weight=4,
 gamma=4,
 subsample=0.8,
 colsample_bytree=.9,
 reg_alpha=0.001,
 #objective= 'binary:logistic',
# nthread=4,
 scale_pos_weight=1,
 #seed=27
 )
#clf1=LogisticRegression(solver='lbfgs',C=1)
#clf1=LinearSVC(C=1,max_iter=1)
#clf2=AdaBoostClassifier(base_estimator=clf1,algorithm='SAMME')
#clf2=AdaBoostClassifier(base_estimator=clf1,algorithm='SAMME')
#clf=BaggingClassifier(base_estimator=clf1,n_estimators=10,max_samples=0.5)

clf.fit(X1,Y1)
#clf2.fit(X1,Y1)
#print("And the score is",clf2.score(X2,Y2))
print("And the score is",clf.score(X2,Y2))


pred=clf.predict(X2)
pred=clf.predict(X2)
print(mean_squared_error(Y2,pred))
print(mean_squared_error(Y2,pred))
submission=pd.DataFrame()
submission['PassengerId'] = test.PassengerId
data1 = test.select_dtypes(include=[np.number]).interpolate().dropna()

X3=data1.drop(['PassengerId'],axis=1)
#submission = pd.DataFrame()
#submission['ID']


ans=clf.predict(X3)
final_predictions = ans
submission['Survived'] = final_predictions

submission.to_csv('result1025.csv', index=False)
