import numpy as np
import pandas as pd
import CSVreader as cr


df = cr.readCSV('Reviews.xlsx')
print(df[0].review)
