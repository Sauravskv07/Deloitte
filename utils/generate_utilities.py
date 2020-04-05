import numpy as np
import pandas as pd
import json

df=pd.read_csv('../data/raw data/Commodity1_price.csv')

df = df.drop_duplicates(subset=['State','Market'])

mapping_index={}
count = 0
for index, row in df.iterrows():
		if(mapping_index.get(row['State'])==None):
			mapping_index[row['State']]={}
		mapping_index[row['State']][row['Market']]=count
		count+=1

json.dump(mapping_index, open("../data/utils/mapping_index.json", 'w' ) )

distance_matrix= np.random.randint(10,1000, size=(count, count))

fuel_array= np.random.rand(count)*5 + 70

np.save('../data/utils/distance_matrix',distance_matrix)

np.save('../data/utils/fuel_matrix',fuel_array)
