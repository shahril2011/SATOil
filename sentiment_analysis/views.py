from django.shortcuts import render
from nltk.sentiment import SentimentIntensityAnalyzer
from .models import Review
from .utils import scrape_website
import nltk
nltk.download('vader_lexicon')
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def analyze_sentiment(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            # Scrape text from the provided URL
            text = scrape_website(url)
            # Perform sentiment analysis using NLTK's SentimentIntensityAnalyzer
            analyzer = SentimentIntensityAnalyzer()
            sentiment_scores = analyzer.polarity_scores(text)
            positive_score = sentiment_scores['pos']
            negative_score = sentiment_scores['neg']
            neutral_score = sentiment_scores['neu']
            if sentiment_scores['compound'] > 0.05:
                sentiment_label = 'Positive'
            elif sentiment_scores['compound'] < -0.05:
                sentiment_label = 'Negative'
            else:
                sentiment_label = 'Neutral'
            # Save review to database
            if request.user.is_authenticated:  # Check if user is authenticated
                user_id = request.user.id  # Get user ID
            else:
                user_id = None  # If user is not authenticated, set user ID to None (guest)
            Review.objects.create(text=text, sentiment=sentiment_label, user_id=user_id)  # Save review with user ID
            return render(request, 'sentiment_analysis/result.html', {'text': text, 'sentiment': sentiment_label, 'positive_score': positive_score, 'negative_score': negative_score, 'neutral_score': neutral_score})
        except Exception as e:
            return render(request, 'sentiment_analysis/error.html', {'error': str(e)})
    else:
        return render(request, 'sentiment_analysis/analyze.html')