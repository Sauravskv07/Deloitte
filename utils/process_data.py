import pandas as pd
import numpy as np

def normalize(df):
	result = df.copy()
	for feature_name in df.columns[df.dtypes.apply(lambda c: np.issubdtype(c, np.number))]:
		if(feature_name=='Label'):
			continue
		else:
			max_value = df[feature_name].max()
			min_value = df[feature_name].min()
			result[feature_name+'_old']=df[feature_name]
			result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
	return result


print("Reading CSV")
df = pd.read_csv('../data/raw data/Commodity1_price.csv')

#print("normalizing data")
#df=normalize(df)

print("Grouping data")
means_stds = df.groupby(['State','Market','Variety','Grade'])['ModalPrice'].agg(['mean','std']).reset_index()
df = df.merge(means_stds,on=['State','Market','Variety','Grade'])

df['Label']=0

df.loc[ df['ModalPrice'] - df['mean'] > df['std'] , 'Label' ]=1
df.loc[ df['mean'] - df['ModalPrice'] > df['std'] , 'Label' ]=-1

df.drop(['mean', 'std'], axis=1)
#df.to_csv('../data/Commodity1_price_updated.csv')

print("Writing the final output")
for label, data in df.groupby(['State','Market','Variety','Grade']):
	data=normalize(data)
	data.fillna(0, inplace=True)
	data.to_csv('../data/csv/Commodity1_price_updated_'+str(label)+".csv")