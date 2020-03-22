import pandas as pd
import numpy as np
from tqdm import tqdm
import os
import math

directory = os.fsencode('../data/csv/')

list_df=[]

for file in os.listdir(directory):
	filename = os.fsdecode(file)
	df=pd.read_csv(os.path.join('../data/csv/', filename))
	if(df.shape[0]!=0):
		list_df.append(df)

#df=pd.read_csv("../data/csv/Commodity1_price_updated_('place1', 'Place0', 'type0','item14').csv")

print("Done Reading Dataframes")

total_size=len(list_df)
train_size=int(total_size*0.7)
test_size=total_size-train_size

X_train = np.zeros((train_size, 4, 100))
Y_train = np.zeros((train_size,1))

print('Total Size',total_size)
print('Train Size',train_size)
print('Test Size',test_size)


print('Constructing Training Set')
for i in tqdm(range(0,train_size)):

	step_count=list_df[i].shape[0]

	if(step_count>100):
		step_count=100

	#print(i, list_df[i].head(2))
	#print(step_count)

	if(step_count==0):
		continue
	X_train[i, :, :step_count] = list_df[i].tail(step_count)[['ModalPrice','MinimumPrice','MaximumPrice','Arrival']].transpose()
	
	Y_train[i,0]=list_df[i].iloc[[step_count-1]]['Label']

print('done TrainingSet')

X_test = np.zeros((test_size, 4, 100))

Y_test = np.zeros((test_size,1))

print('Constructing Test set')
for i in tqdm(range(0,test_size)):
	
	step_count=list_df[i+train_size].shape[0]
	
	if(step_count>100):
		step_count=100

	X_test[i, :, :step_count] = list_df[i+train_size].tail(step_count)[['ModalPrice','MinimumPrice','MaximumPrice','Arrival']].transpose()
	
	Y_test[i,0]=list_df[i+train_size].iloc[[step_count-1]]['Label']


np.save('../data/TrainingSet/' + 'X_train.npy', X_train)
np.save('../data/TrainingSet/' + 'y_train.npy', Y_train)
np.save('../data/TestSet/'+ 'X_test.npy', X_test)
np.save('../data/TestSet/' + 'y_test.npy', Y_test)
