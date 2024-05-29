from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=10)  # Positive, Negative, Neutral
    positive_score = models.FloatField(default=0)
    negative_score = models.FloatField(default=0)
    neutral_score = models.FloatField(default=0)
    time_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Review ID: {self.id}, User ID: {self.user_id}, Sentiment: {self.sentiment}, Date: {self.time_date}"