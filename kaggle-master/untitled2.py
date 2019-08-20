# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:04:32 2019

@author: ONS1KOR
"""
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

submission.to_csv('result1005.csv', index=False)


# =============================================================================
# l=open(r"C:\Users\ons1kor\Automation\Project\other\Kaggle\kaggle-master\result1000.csv","w", newline='')
# writer = csv.writer(l)
# writer.writerow(["Survived"])
# for i in final_predictions:
#     writer.writerow([int(i)])
# =============================================================================

