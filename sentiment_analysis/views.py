from django.shortcuts import render, get_object_or_404, redirect
from nltk.sentiment import SentimentIntensityAnalyzer
from .models import Review
from .utils import scrape_website
import nltk
nltk.download('vader_lexicon')
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib.auth.models import auth

def option(request):
    return render(request, 'sentiment_analysis/option.html')

def analyze_sentiment(request):
    return render(request, 'sentiment_analysis/analyze.html')

@login_required(login_url='member_login')
def analyze_url_sentiment(request):
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
            review = Review.objects.create(
                text=text, 
                sentiment=sentiment_label, 
                positive_score=positive_score,
                negative_score=negative_score,
                neutral_score=neutral_score,
                user=request.user
            )
            return render(request, 'sentiment_analysis/result.html', {
                'text': text, 
                'sentiment': sentiment_label, 
                'positive_score': positive_score, 
                'negative_score': negative_score, 
                'neutral_score': neutral_score
            })
        except Exception as e:
            return render(request, 'sentiment_analysis/error.html', {'error': str(e)})
    else:
        return render(request, 'sentiment_analysis/urlWebsite.html')
    
def analyze_text_sentiment(request):  # Define view for analyzing text sentiment
    if request.method == 'POST':
        text = request.POST.get('text')  # Get the text input from the form
        try:
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
            review = Review.objects.create(
                text=text, 
                sentiment=sentiment_label,
                positive_score=positive_score,
                negative_score=negative_score,
                neutral_score=neutral_score,
                user=request.user
            )
            return render(request, 'sentiment_analysis/result.html', {
                'text': text, 
                'sentiment': sentiment_label, 
                'positive_score': positive_score, 
                'negative_score': negative_score, 
                'neutral_score': neutral_score
            })
        except Exception as e:
            return render(request, 'sentiment_analysis/error.html', {'error': str(e)})
    else:
        return render(request, 'sentiment_analysis/textWebsite.html')
    
@login_required(login_url='member_login')
def review_history(request):
    user_reviews = Review.objects.filter(user=request.user).order_by('-time_date')
    context = {
        'user_reviews': user_reviews
    }
    return render(request, 'sentiment_analysis/review_history.html', context)

@login_required(login_url='member_login')
def sentiment_analysis_result(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    context = {
        'text': review.text,
        'sentiment': review.sentiment,
        'positive_score': review.positive_score,
        'negative_score': review.negative_score,
        'neutral_score': review.neutral_score,
        'id': review.id,
        'timestamp': review.time_date
    }
    return render(request, 'sentiment_analysis/result.html', context)

@login_required(login_url='member_login')
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == "POST":
        review.delete()
        return redirect('review_history')
    return redirect('review_history')