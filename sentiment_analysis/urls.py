from django.urls import path
from . import views

urlpatterns = [
    path('', views.analyze_sentiment, name='analyze_sentiment'),
    path('option/', views.option, name='option'),
    path('analyze_text/', views.analyze_text_sentiment, name='analyze_text_sentiment'),
    path('analyze_url/', views.analyze_url_sentiment, name='analyze_url_sentiment'),
]