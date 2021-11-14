import numpy as np
import pandas as pd

def readCSV(fileName):
    df = pd.read_excel(fileName)
    df = df.values.tolist()

    reviewList = [0 for x in range(len(df[0]))][0 for x in range(len(df))]

    for i in df:
        print(i)
    return df

