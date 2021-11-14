import SentimentAnalyzer as sa
#Class to create an instance of reviews
class Review:
  def __init__(self, list):
    self.review = list[0]
    self.name = list[1]
    self.date = list[2]
    self.sentimentVal = sa.sentimentAnalyzer(list[0]).sentimentScore
    self.memberLength = list[3]
    self.policy = list[4]
    self.policyType = list[5]

  def getReview(self):
    return self.review

  def getName(self):
    return self.name

  def getDate(self):
    return self.date

  def getMemberLength(self):
    return self.memberLength

  def getPolicy(self):
    return self.policy

  def getPolicyType(self):
    return self.policyType

