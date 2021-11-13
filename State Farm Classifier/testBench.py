#Sentiment analyzer testbench
import SentimentAnalyzer

review = 'I have been with State Farm for several years now and see no reason to change. Local agent is great and the service level is unmatched by any of the others that I have used over the years. I routinely check prices and other quotes and the minimal difference is not worth the hassle of changing companies. Claims are handled well and quickly.'
analyzer = SentimentAnalyzer.sentimentAnalyzer.analyzeSentiment(review)

print(analyzer)

