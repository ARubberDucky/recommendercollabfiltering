__author__ = 'Will'

import pandas as pd
import numpy as np

from scipy.spatial.distance import cosine

data = pd.read_csv("C:\\Users\\Will\\Desktop\\ml-1m\\DataSet\\lastfm.csv")
data.head(6).ix[:,1:8]

data_germany = data.drop('user',1)

data_ibs = pd.DataFrame(index=data_germany.columns, columns=data_germany.columns)

#vegan_df = pd.DataFrame(index=df.columns, columns= df.columns)


######################################Let the fun begin#########################################################
#Here we'll find the Cosin Similarity between items
#loop through columns
for i in range(0,len(data_ibs.columns)):
    #compare it with other columns
    for j in range(0, len(data_ibs.columns)):
        data_ibs.ix[i,j] = 1-cosine(data_germany.ix[:,i],data_germany.ix[:,j])

#print data_ibs

# data_neighbors = pd.DataFrame(index=data_ibs.columns,columns=range(1,11))
#
# for i in range(0, len(data_ibs.columns)):
#     data_neighbors.ix[i,:10] = data_ibs.ix[0:,i].sort_values(ascending=True)                       #.order(ascending=False)[:10].index

# Create a placeholder items for closes neighbours to an item
data_neighbours = pd.DataFrame(index=data_ibs.columns,columns=range(1,11))

# Loop through our similarity dataframe and fill in neighbouring item names
for i in range(0,len(data_ibs.columns)):
    data_neighbours.ix[i,:10] = data_ibs.ix[0:,i].sort_values(ascending=False)[:10].index

# --- End Item Based Recommendations --- #




#data_neighbours.head(6)#.ix[:6, 2:4]
#data_neighbours.head(6)
print data_neighbours
print "hello kitty"



