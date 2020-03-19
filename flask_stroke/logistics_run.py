import numpy as np
import pandas as pd
import joblib
from sqlalchemy import create_engine, inspect

classifier_from_joblib = joblib.load('data/log_trained.pkl')
engine = create_engine("sqlite:///stroke.db",echo=False)

ages_raw = engine.execute('select * from age').fetchall()
ages = [(i,a[0]) for i,a in enumerate(ages_raw)]
genders = engine.execute('select * from gender').fetchall()
races = engine.execute('select * from race').fetchall()
conditions = engine.execute('select * from condition').fetchall()
columns = engine.execute('select * from column').fetchall()

column_info = pd.DataFrame(columns).drop(columns=0).rename(columns={1:'columns'})
column_info['values'] = 0
column_info.set_index('columns', inplace=True)

def calculate(age,gender,race,condition):
    column_info['values'] = 0
    age_info = ages[int(age)][1]
    gen_info = genders[int(gender)][1]
    race_info = races[int(race)][1]
    con_info = conditions[int(condition)][1]
    
    for i in range(len(column_info)):
        name = column_info.iloc[i].name
        if name == 'Age':
            column_info.iloc[i,0] = age_info
        elif name == 'Race_'+race_info:
            column_info.iloc[i,0] = 1
        elif name == 'Sex_'+gen_info:
            column_info.iloc[i,0] = 1
        elif name == con_info:
            column_info.iloc[i,0] = 1
            
    user_data_raw = column_info['values'].values
    user_data_rdy = np.array([user_data_raw])
    predict_result = classifier_from_joblib.predict(user_data_rdy)

    print(f"filtered: {age_info},{gen_info},{race_info},{con_info}")
    return f"Prediction Result:\n[0]low chance [1]high chance of stroke\nYour result:{predict_result}"