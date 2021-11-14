# Python program to create a table
from tkinter import *
from CSVreader import readCSV

class Table:
    def __init__(self, lst):
        totalRows = len(lst)
        totalCols = len(lst[0])

        root = Tk()
        root.title('State Farm Sentiment Calculator')
        root.configure(bg='black')
        for i in range(totalRows):
            for j in range(totalCols):
                self.e = Entry(root, width=50, fg='black',font=('Arial', 12, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
        root.mainloop()