import pandas as pd
import numpy as np
from tqdm import tqdm
import os
import math

directory = os.fsencode('../data/csv/')

list_df=[]

test_size=0

for file in os.listdir(directory):
	filename = os.fsdecode(file)
	df=pd.read_csv(os.path.join('../data/csv/', filename))
	
	if(df.shape[0]>10):
		test_size+=1

	if(df.shape[0]!=0):
		list_df.append(df)

#df=pd.read_csv("../data/csv/Commodity1_price_updated_('place1', 'Place0', 'type0','item14').csv")
train_size=len(list_df)
total_size=train_size


print("Done Reading Dataframes")

X_train = np.zeros((train_size, 4, 10))
Y_train = np.zeros((train_size,1))

print('Total Size',total_size)
print('Train Size',train_size)
print('Test Size',test_size)


print('Constructing Training Set')

for i in tqdm(range(0,train_size)):

	step_count=list_df[i].shape[0]

	if(step_count>10):
		step_count=10

	if(step_count==0):
		continue

	X_train[i, :, :step_count] = list_df[i].tail(step_count)[['ModalPrice','MinimumPrice','MaximumPrice','Arrival']].transpose()
	
	Y_train[i,0]=list_df[i].iloc[[step_count-1]]['Label']

print('Done Constructing Training Set')

X_test = np.zeros((test_size, 4, 10))
Y_test = np.zeros((test_size,1))

print('Constructing Test set')

j=0

for i in tqdm(range(0,test_size)):
	
	step_count=list_df[j].shape[0]

	if(step_count<=10):
		j+=1
		continue

	if(step_count>20):
		step_count=20

	#print(step_count)
	X_test[i, :, :step_count-10] = list_df[j].iloc[-step_count:-10][['ModalPrice','MinimumPrice','MaximumPrice','Arrival']].transpose()
	Y_test[i,0]=list_df[j].iloc[[step_count-1]]['Label']
	j+=1


np.save('../data/TrainingSet/' + 'X_train.npy', X_train)
np.save('../data/TrainingSet/' + 'y_train.npy', Y_train)
np.save('../data/TestSet/'+ 'X_test.npy', X_test)
np.save('../data/TestSet/' + 'y_test.npy', Y_test)
