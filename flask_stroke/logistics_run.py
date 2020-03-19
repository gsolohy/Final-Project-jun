import numpy as np
import joblib
from sqlalchemy import create_engine, inspect

classifier_from_joblib = joblib.load('data/log_trained.pkl')
engine = create_engine("sqlite:///stroke.db",echo=False)

def callin_db():
    ages = engine.execute('select * from age').fetchall()
    genders = engine.execute('select * from gender').fetchall()
    races = engine.execute('select * from race').fetchall()
    conditions = engine.execute('select * from condition').fetchall()
    return ages, genders, races, conditions

#args => age,gender,ethnicity,condition
def calculate():
    testdummy_data0 = np.array([[55,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0]]) # take in posted info
    testdummy_data1 = np.array([[55,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1]])
    predict_result0 = classifier_from_joblib.predict(testdummy_data0) # run and save to variable
    predict_result1 = classifier_from_joblib.predict(testdummy_data1)

    print(r"Result: LowStroke [0] or HighStroke [1]")
    print(f"55 years old/caucasian/male/no condition:  {predict_result0}")
    print(f"55 years old/caucasian/male/all(5) condition:  {predict_result1}")

    return predict_result0
