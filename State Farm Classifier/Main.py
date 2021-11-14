from CSVreader import readCSV
import UI
reviews = readCSV('Reviews.xlsx')

#print(vars(reviews[0]))
for i in reviews:
    print(vars(i))

