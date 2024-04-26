from django.db import models

from django.db import models

class Review(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=10)  # Positive, Negative, Neutral