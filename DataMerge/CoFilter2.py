__author__ = 'Will'

import pandas as pd
import numpy as np

from scipy.spatial.distance import cosine

def getScore(history,similarities):
    return sum(history*similarities)/sum(similarities)




names = np.load("C:\\Users\\Will\\Desktop\\ml-1m\\DataSet\\NameMatrix.npy")
valuematrix = np.load("C:\\Users\\Will\\Desktop\\ml-1m\\DataSet\\ArrangedMatrix.npy")


df = pd.DataFrame(valuematrix, columns=np.array(names).tolist())



df = df.drop('0',1)
#df = df.drop(df.head(1).index)
#print df



data_ibs = pd.DataFrame(index=df.columns, columns= df.columns)


######################################Let the fun begin#########################################################
#Here we'll find the Cosin Similarity between items
#loop through columns
for i in range(0,len(data_ibs.columns)):
    #compare it with other columns
    for j in range(0, len(data_ibs.columns)):
        data_ibs.ix[i,j] = 1-cosine(df.ix[:,i],df.ix[:,j])


data_neighbours = pd.DataFrame(index=data_ibs.columns,columns=range(1,11))

# Loop through our similarity dataframe and fill in neighbouring item names
for i in range(0,len(data_ibs.columns)):
    data_neighbours.ix[i,:10] = data_ibs.ix[0:,i].sort_values(ascending=False)[:10].index

# --- End Item Based Recommendations --- #


print data_neighbours


#User Layer#

data_simulated = pd.DataFrame(index=df.index, columns=df.columns)

print "hi1"
#fill in username column
data_simulated.ix[:,:1] = df.ix[:,:1]
print "hi2"
for i in range(0, len(data_simulated.index)):
    for j in range(1, len(data_simulated.columns)):
        user = data_simulated.index[i]
        product = data_simulated.columns[j]

        if df.ix[i][j] == 1:
            data_simulated.ix[i][j] = 0
        else:
            product_top_names = data_neighbours.ix[product][1:10]
            product_top_sims = data_ibs.ix[product].sort_values(ascending=False)[1:10];
            user_purchases = df.ix[user, product_top_names]

            data_simulated.ix[i][j] = getScore(user_purchases, product_top_sims)



for i in range(0, len(data_simulated.index)):
    for j in range(1, len(data_simulated.columns)):
        if df.ix[i][j] == 1:
            data_simulated.ix[i][j] = 0




print "hi3 "

data_recommend = pd.DataFrame(index=data_simulated.index, columns=['user', '1', '2', '3', '4', '5', '6'])
data_recommend.ix[0:,0] = data_simulated.ix[:,0]
print "hi4"
for i in range(0, len(data_simulated.index)):
    data_recommend.ix[i,1:] = data_simulated.ix[i,:].sort_values(ascending=False).ix[1:7,].index.transpose()


print "kitty"
print data_recommend.ix[:10,:4]

data_recommend.to_csv('C:\\Users\\Will\\Desktop\\ml-1m\\DataSet\\example2.csv')



print "hello kitty"



