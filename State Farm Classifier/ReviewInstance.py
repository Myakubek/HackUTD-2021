import SentimentAnalyzer as sa

#Class to create an instance of reviews
class Review:
  def __init__(self, review, name, date, memberLength, policy, policyType):
    self.review = review
    self.name = name
    self.date = date
    self.sentimentVal = sa.sentimentAnalyzer(review)
    self.memberLength = memberLength
    self.policy = policy
    self.policyType = policyType

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

  