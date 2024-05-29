from django.core.management.base import BaseCommand
from django.utils import timezone
from sentiment_analysis.models import Review

class Command(BaseCommand):
    help = 'Delete sentiment analyses associated with guest users older than 24 hours'

    def handle(self, *args, **kwargs):
        # Define the threshold time (24 hours ago)
        threshold_time = timezone.now() - timezone.timedelta(hours=24)
        
        # Delete reviews associated with guest users older than the threshold time
        deleted_count, _ = Review.objects.filter(user_id=None, time_date__lt=threshold_time).delete()
        
        self.stdout.write(self.style.SUCCESS(f'{deleted_count} sentiment analyses associated with guest users were deleted.'))