import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Tag(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField(max_length=278)
    created_at = models.DateTimeField("date published", auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def was_posted_today(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.text[:20]
