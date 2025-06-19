import pandas as pd

def getResults(week, names)->list[list[int],str]:
    second = pd.read_csv(f'gws/gw{week+1}.csv')
    res = [[],[]]
    for index,name in enumerate(names):
        if name not in second['name'].value:
            second = second.drop(index).reset_index(drop=True)
            name.remove
    for i in range(len(second)):
        res[0].append(second.iloc[i].xP)
        res[1].append(second.at[i,'name'])
    return res