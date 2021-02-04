from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    for_day = models.CharField(max_length=255)
    to_day = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
