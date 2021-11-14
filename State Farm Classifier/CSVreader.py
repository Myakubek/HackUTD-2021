import pandas as pd
from ReviewInstance import Review

def readCSV(fileName):
    df = pd.read_excel(fileName)
    df = df.values.tolist()
    reviews = []

    for i in df:
        reviews.append(Review(i))
    return reviews
