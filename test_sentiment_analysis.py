import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):

    def test_sentiment_analyzer(self):
        response = sentiment_analyzer('I love working with Python')
        self.assertEqual(response['label'], 'SENT_POSITIVE')

        response = sentiment_analyzer('I hate working with Python')
        self.assertEqual(response['label'], 'SENT_NEGATIVE')

        response = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(response['label'], 'SENT_NEUTRAL')

unittest.main()