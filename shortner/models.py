from django.db import models
from django.utils import timezone

class Link(models.Model):
    url = models.CharField(max_length=200)
    hash = models.CharField(max_length=20)
    published_date = models.DateTimeField(blank=True,null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()