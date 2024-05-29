from django.urls import path
from . import views

urlpatterns = [
    path('', views.analyze_sentiment, name='analyze_sentiment'),
    path('option/', views.option, name='option'),
    path('analyze_text/', views.analyze_text_sentiment, name='analyze_text_sentiment'),
    path('analyze_url/', views.analyze_url_sentiment, name='analyze_url_sentiment'),
    path('review-history/', views.review_history, name='review_history'),
    path('review/<int:review_id>/result/', views.sentiment_analysis_result, name='sentiment_analysis_result'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
]