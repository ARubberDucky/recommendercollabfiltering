from __future__ import print_function
__author__ = 'Will'


import os
import subprocess
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz



def get_data():
    if os.path.exists("C:\\Users\\Will\\Desktop\\ml-1m\\DataSet\\mergedData.csv"):
        print ("Dataset found")
        df = pd.read_csv("C:\\Users\\Will\\Desktop\\ml-1m\\DataSet\\mergedData.csv", header=0, index_col=0)
    else:
        print("No file found")
        exit()
    return df
# def encode_column(df, column):
#     modified = df.copy()
#     targetCol = modified[column].unique()
#     map_to_int = {name: n for n, name in enumerate(targetCol)}
#
#
#     modified["Target"] = modified[column].replace(map_to_int)
#     return (modified, targetCol)
def encode_column(df, target_column, newrow):

    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    # df_mod["Target"] = df_mod[target_column].replace(map_to_int)
    df_mod[newrow] = df[target_column].map(map_to_int)

    return (df_mod, targets)


df = get_data()
#print("Head", df.head(), sep="\n", end="\n\n" )
#print ("Tail", df.tail(),  sep="\n", end="\n\n" )


#print("* ratings", df["Rating"].unique() ,sep="\n")

df2, TitleValues = encode_column(df, "Title","TitleCoded")
df2, GenreValues = encode_column(df2, "Genres", "GenreCoded")
df2, GenderValues = encode_column(df2, "Gender", "GenderCoded")
print("* df.head()", df2[["TitleCoded","Title"]].head(), sep="\n", end="\n\n")
print("* df.tail()", df2[["TitleCoded","Title"]].tail(), sep="\n", end="\n\n")


print("* df.head()", df2[["GenreCoded","Genres"]].head(), sep="\n", end="\n\n")
print("* df.tail()", df2[["GenreCoded","Genres"]].tail(), sep="\n", end="\n\n")

print (TitleValues)