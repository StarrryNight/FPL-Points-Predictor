import pandas as pd
import seaborn as sns
from sklearn import linear_model
#data preprocessing


def guess(data, predictor, target_dat, result, evaluationMetric)-> list[list[int],list[int],list[str] ]:
    res= [[],[],[]]
    
    #remove ireelaventstuff
    data.drop([], axis=1, inplace=True)

    #new parameters
    data['opponent_index'], data['result'] = 0,0
    target_dat['opponent_index'], target_dat['result'] = 0,0
    
   
    #write new variable using difference between home and away teams and Compute next week performance
    for i in range(len(data)):
        data.at[i,'result'] = predictor.at[i, 'total_points']
        if data.iloc[i].was_home == True:
            data.at[i,'opponent_index'] = data.iloc[i].team_h_score - data.iloc[i].team_a_score
        else:
            data.at[i,'opponent_index']   = data.iloc[i].team_a_score - data.iloc[i].team_h_score

    
    reg = linear_model.LinearRegression()
   
    reg.fit(data[evaluationMetric], data.result)
    
    for playerID in range(len(result)):
        temp = []
        for criteria in evaluationMetric:
            temp.append([target_dat.at[playerID, criteria]][0])
        res[0].append(reg.predict([temp])[0])
        res[1].append(result.at[playerID, 'total_points'])
        res[2].append(target_dat.at[playerID,'name'])
    print(reg.coef_)
    print(len(predictor))
    return res

#[target_dat.at[playerID,'xP'],target_dat.at[playerID,'bonus'], target_dat.at[playerID,'bps'], target_dat.at[playerID,'influence'], target_dat.at[playerID,'minutes' ], target_dat.at[playerID,'total_points'], target_dat.at[playerID,'opponent_index']] 