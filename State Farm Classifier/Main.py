from CSVreader import readCSV
reviews = readCSV('Reviews.xlsx')

def printReviews(lst):
    for i in lst:
        print('Name:', i.name, '   Date:', i.date, '   Member for', i.memberLength, 'days')
        print('Policy:', i.policy, '   Policy Type:', i.policyType, '   Feedback positivity:', i.sentimentVal)
        print ("Review: ", i.review)
        print()


pos = []
neg = []

for i in reviews:
    if i.sentimentVal[0] == '-':
        neg.append(i)
    else:
        pos.append(i)

print("---Positive values---")
printReviews(pos)
print()

print("---Negative values--")
printReviews(neg)




