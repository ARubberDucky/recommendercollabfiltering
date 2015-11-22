__author__ = 'Will'

import pandas as pd
import numpy

mergedData = pd.read_csv("C:\\Users\\Will\\Desktop\\ml-1m\\DataSet\\mergedData.csv")
mergedData.drop(mergedData.columns[[1,2,3,4,7,9]], axis=1, inplace=True)
user_Ratings = {}

gb = mergedData.groupby('UserID')

groups = dict(list(mergedData.groupby(['UserID'])))

print len(groups)

# for user in range(0, len(groups)):
#     temp = groups[user]
#     listofTuples = {}
#     for i in range(0, len(temp)):
#


#temp = groups[1]


# for i in range(0, len(temp)):
#     print  temp['Title'][i], temp['Rating'][i]





