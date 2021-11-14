from CSVreader import readCSV
import pprint as pp
reviews = readCSV('Reviews.xlsx')

#print(vars(reviews[0]))
for i in reviews:
    pp.pprint(vars(i))

