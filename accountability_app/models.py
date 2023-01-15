import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings


class Post(models.Model):
    post_text = models.TextField(max_length=278)
    pub_date = models.DateTimeField("date published")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def was_posted_today(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.post_text[:20]
