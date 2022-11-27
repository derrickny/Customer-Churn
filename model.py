#import the required libraries
import pandas as pd
import numpy as np 
import pickle

#load the data 
df = pd.read_csv(" Churn_Modelling.csv")

#dropping columns that wont be needed 
df.drop(['RowNumber','CustomerId','Surname'], axis=1, inplace=True)

#preprocessing data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder , StandardScaler
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

#lets perfrom preprocessing on geography
df['Geography'] = le.fit_transform(df['Geography'])  

#changing to type string the outcome column Exited
df['Exited'] = df['Exited'].astype(str)
#replacing the outcome Exited outcome to 1-exited 
df['Exited'] = df['Exited'].str.replace('1', 'Exited')
df['Exited'] = df['Exited'].str.replace('0', 'Remained')

#Define X and Y
x = df.drop('Exited',axis = 1)
y = df['Exited']

#Divide the data into training and testing 
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.23)


#scaling 
sc = StandardScaler()
sc.fit_transform(x_train)
sc.transform(x_test)

#creating a model and perfroming training 
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(solver='liblinear', C=0.05, multi_class='ovr',
                           random_state=0)
model.fit(x_train, y_train)

#Make pickle file of our model
pickle.dump(model, open("model.pkl", "wb"))
