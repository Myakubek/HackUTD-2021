import numpy as np
import pandas as pd
import CSVreader as cr


df = cr.readCSV('Reviews.xlsx')
for i in df:
    print(i.review)
    print(i.date)
