from django.shortcuts import render, get_object_or_404, redirect
from nltk.sentiment import SentimentIntensityAnalyzer
from .models import Review
from .utils import scrape_website
import nltk
nltk.download('vader_lexicon')
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import auth

from wordcloud import WordCloud
import io
import base64

def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    buf = io.BytesIO()
    wordcloud.to_image().save(buf, format='PNG')
    byte_im = buf.getvalue()
    return base64.b64encode(byte_im).decode()

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

            word_count = len(text.split())
            word_cloud_image = generate_word_cloud(text)

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
                'neutral_score': neutral_score,
                'word_count': word_count,
                'word_cloud_image': word_cloud_image
            })
        except Exception as e:
            return render(request, 'sentiment_analysis/error.html', {'error': str(e)})
    else:
        return render(request, 'sentiment_analysis/urlWebsite.html')
    
def analyze_text_sentiment(request):
    if request.method == 'POST':
        text = request.POST.get('text')
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
            
            word_count = len(text.split())
            word_cloud_image = generate_word_cloud(text)

            # Save review to database
            user = request.user if request.user.is_authenticated else None
            context = {
                'text': text,
                'sentiment': sentiment_label,
                'positive_score': positive_score,
                'negative_score': negative_score,
                'neutral_score': neutral_score
            }

            # Check if user is authenticated to include word cloud
            if request.user.is_authenticated:
                user_id = request.user.id  # Get user ID
                Review.objects.create(
                    text=text, 
                    sentiment=sentiment_label, 
                    user=user,
                    positive_score=positive_score,
                    negative_score=negative_score,
                    neutral_score=neutral_score
                    )
                word_cloud_image = generate_word_cloud(text)
                context['word_cloud_image'] = word_cloud_image
                context['show_visualization'] = True
            else:
                context['show_visualization'] = False

            return render(request, 'sentiment_analysis/result.html', context)
        except Exception as e:
            return render(request, 'sentiment_analysis/error.html', {'error': str(e)})
    else:
        return render(request, 'sentiment_analysis/textWebsite.html')
    
@login_required
def review_history(request):
    if request.user.is_superuser:
        user_reviews = Review.objects.all().order_by('-time_date')
    else:
        user_reviews = Review.objects.filter(user=request.user).order_by('-time_date')
    sentiments_over_time = user_reviews.values_list('time_date', 'positive_score', 'negative_score', 'neutral_score')
    context = {
        'user_reviews': user_reviews,
        'sentiments_over_time': list(sentiments_over_time),
        'is_admin': request.user.is_superuser
    }
    return render(request, 'sentiment_analysis/review_history.html', context)

@login_required(login_url='member_login')
def sentiment_analysis_result(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if not request.user.is_superuser and review.user != request.user:
        return redirect('review_history')
    word_cloud_image = generate_word_cloud(review.text)
    context = {
        'text': review.text,
        'sentiment': review.sentiment,
        'positive_score': review.positive_score,
        'negative_score': review.negative_score,
        'neutral_score': review.neutral_score,
        'id': review.id,
        'timestamp': review.time_date,
        'word_cloud_image': word_cloud_image
    }
    return render(request, 'sentiment_analysis/result.html', context)

@login_required(login_url='member_login')
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if not request.user.is_superuser and review.user != request.user:
        return redirect('review_history')
    if request.method == "POST":
        review.delete()
        return redirect('review_history')
    return redirect('review_history')