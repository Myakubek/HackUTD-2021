import numpy as np
import pandas as pd
from SentimentAnalyzer import *
from ReviewInstance import *

def readCSV(fileName):
    df = pd.read_excel(fileName)
    df = df.values.tolist()

    reviewList = [0 for x in range(len(df[0]))][0 for x in range(len(df))]

    for i in df:
        print(i)
    return df

l = reviewlist.size()

vehicleList = [l][]
homeList = [l][]
lifeList = [l][]
healthList = [l][]
smallBusinessList = [l][]
policyList = [vehicleList, homeList, lifeList, healthList, smallBusinessList]

    for (x = 0; x < l; x++):
        post = Review()
        post.review = reviewList[x][0]
        post.reviewerName = reviewList[x][1]
        post.date = reviewList[x][2]
        post.rmemberLength = reviewList[x][3]
        post.policy = reviewList[x][4]
        post.policyType = reviewList[x][5]
        
        if (post.policy == "Vehicle"):
            vehicleList.append(post)
        if (post.policy == "Home"):
            homeList.append(post)
        if (post.policy == "Life"):
            lifeList.append(post)
        if (post.policy == "Health"):
            healthList.append(post)
        if (post.policy = "Small Business"):
            smallBusinessList.append(post)
        
        posVal = getPositive(self, post.review)
        negVal = getNegative(self, post.review)
        
        if (posVal > negVal):
            post.sentimentVal = posVal
        else if (negVal > posVal):
            negVal = negVal * -1.0
            post.sentimentVal = negVal
        else:
            post.sentimentVal = 0.0
            
return policyList
