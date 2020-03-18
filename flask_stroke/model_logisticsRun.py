import numpy as np
import joblib

classifier_from_joblib = joblib.load('data/log_trained.pkl')

testdummy_data0 = np.array([[55,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0]])
testdummy_data1 = np.array([[55,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1]])
predict_result0 = classifier_from_joblib.predict(testdummy_data0)
predict_result1 = classifier_from_joblib.predict(testdummy_data1)
print(r"Result: LowStroke [0] or HighStroke [1]")
print(f"55 years old/caucasian/male/no condition:  {predict_result0}")
print(f"55 years old/caucasian/male/all(5) condition:  {predict_result1}")