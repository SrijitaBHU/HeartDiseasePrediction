import pandas as pd
import numpy as np
data1=pd.read_csv('data1.csv')
a = list(data1.columns[:13])
x = data1[a].values
y = data1['num'].values
from sklearn.svm import SVC,LinearSVC
final_model = SVC()
final_model.fit(x,y)
d = map(float,raw_input().split())
c = []
c.append(d)
t = (final_model.predict(c))
print (t)
if(t==1):
    print ("Mild Disease (>50% diameter narrowing)")
elif(t==2):
    print ("Moderate or Severe disease")
elif(t==3):
    print ("Critical Condition")
elif(t==4):
    print ("Heart Failure")
else:
    print ("Normal Heart(<50% diameter narrowing)")
