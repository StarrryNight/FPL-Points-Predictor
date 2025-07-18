import pandas as pd
def handleCleanup(week_data, target)->list:
    data = pd.read_csv(f'gws/gw{week_data}.csv')
    predictor = pd.read_csv(f'gws/gw{week_data+1}.csv')

    target_dat =pd.read_csv(f'gws/gw{target}.csv')
    result = pd.read_csv(f'gws/gw{target+1}.csv')

    print(f'{len(data)} {len(target_dat)} {len(result)} {len(predictor)}')
    target_dat.drop_duplicates(inplace=True, subset='name')
    target_dat.reset_index(inplace=True)
    data.drop_duplicates(inplace=True, subset='name', keep='first')
    data.reset_index(inplace=True)
    result.drop_duplicates(inplace=True, subset='name')
    result.reset_index(inplace=True)
    predictor.drop_duplicates(inplace=True, subset='name')
    predictor.reset_index(inplace=True)
    print(f'{len(data)} {len(target_dat)} {len(result)} {len(predictor)}')
    count =0
    while count<len(data):
        if  data.at[count, 'name'] not in target_dat['name'].values or data.at[count, 'name'] not in predictor['name'].values or data.at[count, 'name'] not in result['name'].values:
            data = data.drop(count)
            data.reset_index(drop=True, inplace=True)
        else:
            count+=1
            

    count = 0
    
    while count<len(target_dat):
        if (target_dat.at[count, 'name'] not in data['name'].values) or (target_dat.at[count, 'name'] not in result['name'].values) or (target_dat.at[count, 'name'] not in predictor['name'].values) :
            target_dat.drop(count,inplace=True)
            target_dat.reset_index(drop=True, inplace=True)
        else:
            count+=1
    count =0   
    
    while count<len(predictor):
        if predictor.at[count, 'name'] not in target_dat['name'].values or predictor.at[count, 'name'] not in data['name'].values or predictor.at[count, 'name'] not in result['name'].values:
            predictor = predictor.drop(count).reset_index(drop=True)
        else:
            count+=1
    
    count = 0
    
    while count<len(result):
        if result.at[count, 'name'] not in target_dat['name'].values or result.at[count, 'name'] not in data['name'].values or result.at[count, 'name'] not in predictor['name'].values:
     
            result= result.drop(index =count)
            result.reset_index(drop=True, inplace=True)
        else:
            count+=1
    print(f'{len(data)} {len(target_dat)} {len(result)} {len(predictor)}')
    count =0
    
    return [data,predictor,target_dat, result]