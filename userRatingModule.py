import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

def userRating(top, bottom, shoes):
    df = pd.read_csv("/workspace/flaskPrc/dataUserRatingFF.csv")

    df.rename(columns={'Unnamed: 0' : 'top', 'Unnamed: 1' : 'bottom', 'Unnamed: 2' : 'shoes'},inplace=True)
    df.set_index(['top','bottom','shoes'], inplace=True)

    dfResult = cosine_similarity(df)
    dfResult = pd.DataFrame(data = dfResult, index=df.index, columns = df.index)

    dfResult = dfResult[top][bottom][shoes].sort_values(ascending=False).to_frame()[0:]


    realResult = dfResult.reset_index()
    realResult.columns = ['top', 'bottom', 'shoes', 'rating']

    # dict_result = {}

    # for idx, row in realResult.head(3).iterrows():
    #   dict_result[idx] = {
    #     'set': {
    #       'top': row['top'],
    #       'bottom' : row['bottom'],
    #       'shoes' : row['shoes']
    #       },
    #     'rating': row['rating']
    #   }
    #   print(dict_result)

    js = realResult.to_json(orient = 'records')
    print(js)

    return js
