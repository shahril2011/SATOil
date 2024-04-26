from django.shortcuts import render
from nltk.sentiment import SentimentIntensityAnalyzer
from .models import Review
from .utils import scrape_website
import nltk
nltk.download('vader_lexicon')

def analyze_sentiment(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            # Scrape text from the provided URL
            text = scrape_website(url)
            # Perform sentiment analysis using NLTK's SentimentIntensityAnalyzer
            analyzer = SentimentIntensityAnalyzer()
            sentiment_score = analyzer.polarity_scores(text)['compound']
            if sentiment_score > 0.05:
                sentiment_label = 'Positive'
            elif sentiment_score < -0.05:
                sentiment_label = 'Negative'
            else:
                sentiment_label = 'Neutral'
            # Save review to database
            Review.objects.create(text=text, sentiment=sentiment_label)
            return render(request, 'sentiment_analysis/result.html', {'text': text, 'sentiment': sentiment_label, 'sentiment_score': sentiment_score})
        except Exception as e:
            return render(request, 'sentiment_analysis/error.html', {'error': str(e)})
    else:
        return render(request, 'sentiment_analysis/analyze.html')