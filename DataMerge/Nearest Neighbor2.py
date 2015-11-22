__author__ = 'Will'

import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

from scipy.spatial.distance import cosine


names = np.load("C:\\Users\\Will\\Desktop\\ml-1m\\DataSet\\NameMatrix.npy")
valuematrix = np.load("C:\\Users\\Will\\Desktop\\ml-1m\\DataSet\\ArrangedMatrix.npy")


#df = pd.DataFrame(valuematrix, columns=np.array(names).tolist())


nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(valuematrix)
distances,indeces = nbrs.kneighbors(valuematrix)
#print indeces
#print distances

temp = nbrs.kneighbors_graph(valuematrix).toarray()
print temp

# df = df.drop('0',1)
# #df = df.drop(df.head(1).index)
# #print df
#
#
#
# data_ibs = pd.DataFrame(index=df.columns, columns= df.columns)
#
#
# ######################################Let the fun begin#########################################################
# #Here we'll find the Cosin Similarity between items
# #loop through columns
# for i in range(0,len(data_ibs.columns)):
#     #compare it with other columns
#     for j in range(0, len(data_ibs.columns)):
#         data_ibs.ix[i,j] = 1-cosine(df.ix[:,i],df.ix[:,j])
#
#
# data_neighbours = pd.DataFrame(index=data_ibs.columns,columns=range(1,11))
#
# # Loop through our similarity dataframe and fill in neighbouring item names
# for i in range(0,len(data_ibs.columns)):
#     data_neighbours.ix[i,:10] = data_ibs.ix[0:,i].sort_values(ascending=False)[:10].index
#
# # --- End Item Based Recommendations --- #
#
#
#
# print data_neighbours
# print "hello kitty"



