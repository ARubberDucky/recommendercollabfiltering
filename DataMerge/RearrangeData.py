__author__ = 'Will'


import pandas as pd
import numpy
import h5py


users = pd.read_csv("C:\\Users\\Will\\Desktop\\ml-1m\\users.csv")
movies = pd.read_csv("C:\\Users\\Will\\Desktop\\ml-1m\\movies.csv")
ratings = pd.read_csv("C:\\Users\\Will\\Desktop\\ml-1m\\ratings.csv")

#Matrix = [[0 for x in range(0, 3953)] for x in range(0,6041)]
Matrix = numpy.zeros((6041, 3953), dtype=int)
NameMatrix = {}
#NameMatrix[0] = 0
temp = users.as_matrix()

# for i in range(1, 6041):
#     trimval = temp[i-1][0]
#     Matrix[i][0] = int(trimval)


temp = movies.as_matrix()
filler = 0
NameMatrix[0] = '0'
for i in range(1,3953):
    tempitem = temp[i-filler-1][0]

    if(i != temp[i-filler][0]):
        NameMatrix[i] = 'unk' + str(filler)
        filler += 1
    else:
        NameMatrix[i] = temp[i-filler][1]

    # elif(int(temp[tempitem][0]) == (tempitem)):
    #     NameMatrix[i] = temp[i-filler][1]
    # else:
    #     NameMatrix[i] = 'unk' + str(filler)
    #     filler += 1

NameMatrix[1] = 'Toy Story (1995)'
temp = ratings.as_matrix();

matrixX = 1
matrixY = 1

#print len(Matrix[2])
for(x,y), value in numpy.ndenumerate(temp):
    user = int(temp[x][0])
    movie = int(temp[x][1])
    #print user
    #print movie
    #this is where logic would go
    Matrix[user][movie] = 1



print Matrix[0]
print Matrix[1]
print Matrix[2]
print Matrix[3]
#print NameMatrix
print NameMatrix
#print Matrix.__sizeof__()

#numpy.savez_compressed("C:\\Users\\Will\\Desktop\\ml-1m\\DataSet\\ArrangedMatrix.txt", Matrix)
#datadump = pd.HDFStore("C:\\Users\\Will\\Desktop\\ml-1m\\DataSet\\ArrangedMatrix.hdf")
#datadump.append("Matrix", pd.DataFrame(Matrix))
#datadump.close()

numpy.save("C:\\Users\\Will\\Desktop\\ml-1m\\DataSet\\ArrangedMatrix",Matrix)
numpy.save("C:\\Users\\Will\\Desktop\\ml-1m\\DataSet\\NameMatrix", NameMatrix.values())