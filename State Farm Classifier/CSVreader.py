import pandas as pd
from ReviewInstance import Review

def readCSV(fileName):
    df = pd.read_excel(fileName)
    df = df.values.tolist()
    reviews = []

    for i in df:
<<<<<<< HEAD
        reviews.append(Review(i))
    return reviews
=======
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
        
        
            
>>>>>>> 888cd10d1514e897552a4d0911fbd976e1743b60
