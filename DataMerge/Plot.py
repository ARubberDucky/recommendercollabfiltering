__author__ = 'Will'

import pandas as pd
import numpy as np

from scipy.spatial.distance import cosine

import matplotlib
#matplotlib.style.use('ggplot')

names = np.load("C:\\Users\\Will\\Desktop\\ml-1m\\DataSet\\NameMatrix.npy")
valuematrix = np.load("C:\\Users\\Will\\Desktop\\ml-1m\\DataSet\\ArrangedMatrix.npy")


df = pd.DataFrame(valuematrix, columns=np.array(names).tolist())
df.plot(kind= 'bar', stacked=True)
