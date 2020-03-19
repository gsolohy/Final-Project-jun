#import libraries
import numpy as np
import pandas as pd

# Read the csv file into a pandas DataFrame
data = pd.read_csv('data/data_adan.csv')

#Convert categorical data into dummy data 
data = pd.get_dummies(data)

#define X and y
X = data[['Age','Race_AI', 'Race_AS', 'Race_BL', 'Race_CA', 'Race_HI', 'Race_NH', 'Race_OT', 'Race_PI', 'Race_UNK', 'Sex_F', 'Sex_M', 'HTN', 'Dyslipidemia', 'Carotid stenosis', 'CKD', 'DM']]
y = data["Stroke"].values.reshape(-1, 1)

# Split the data into training and testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Create a StandardScater model and fit it to the training data
from sklearn.preprocessing import StandardScaler
X_scaler = StandardScaler().fit(X_train)
y_scaler = StandardScaler().fit(y_train)

# Transform the training and testing data using the X_scaler and y_scaler models
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
y_train_scaled = y_scaler.transform(y_train)
y_test_scaled = y_scaler.transform(y_test)

#import logistic regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()

#fit the data
classifier.fit(X_train, y_train)

new_data = np.array([[55,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1]])
predictions = classifier.predict(new_data)
print("Classes are either 0 (No Stroke) or 1 (Stroke)")
print(f"The new point was classified as: {predictions}")

import pickle
# Save the trained model as a pickle string.
saved_model = pickle.dumps(classifier)

# Load the pickled model 
classifier_from_pickle = pickle.loads(saved_model)

# Use the loaded pickled model to make predictions 
predictions2 = classifier_from_pickle.predict(new_data)
print("Classes are either 0 (No Stroke) or 1 (Stroke)")
print(f"The new point was classified as: {predictions2}")

import joblib
joblib.dump(classifier, 'data/log_trained.pkl')
classifier_from_joblib = joblib.load('data/log_trained.pkl')
predictions3 = classifier_from_joblib.predict(new_data)
print("Classes are either 0 (No Stroke) or 1 (Stroke)")
print(f"The new point was classified as: {predictions3}")