#imports
import nltk
import nltk.data
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
nltk.download('punkt', quiet = True)
nltk.download('vader_lexicon', quiet = True)
nltk.download('stopwords', quiet = True)

class sentimentAnalyzer:
    #Function to convert a list to string for stopword formatting/conversion
    def __init__(self, text):
        self.text = text
        self.sentimentScore = self.getSentiment(text)

    def listToString(self, string):
        str = ""
        for s in string:
            str += s
            str += " "
        return str

    #Gets a string, splits into a list and filters out stopwards, returns formatted string
    def removeStopwords(self, Text):
        Text = Text.split(" ")                                  #Split text into seperated list
        stopwords = nltk.corpus.stopwords.words("english")           #import a list of stopwords from nltk
        Text = [w for w in Text if w.lower() not in stopwords]       #Remove the stopwords from Text (becomes list of words)
        return self.listToString(Text)


    #Use nltk's pre-trained sentiment analyzer (VADER) to analyze a given text
    def analyze(self, input):
        sia = SentimentIntensityAnalyzer()    #Instantiate sentiment analyzer object
        input = self.removeStopwords(input)
        scores = sia.polarity_scores(input)   #Returns a dictionary of sentiment scores
        return scores


    def getNegative(self, text):
        return (format(self.analyze(text).get('neg') * 100, '.1f'))


    def getPositive(self, text):
        return (format(self.analyze(text).get('pos') * 100, '.1f'))

    def getSentiment(self, text):
        if float(self.getPositive(text)) > float(self.getNegative(text)):
            return str(float(self.getPositive(text)) - float(self.getNegative(text))) + '%'
        else:
            return str(float(self.getPositive(text)) - float(self.getNegative(text))) + '%'