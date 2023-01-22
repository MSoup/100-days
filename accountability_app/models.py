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
    post_text = models.TextField(max_length=278)
    pub_date = models.DateTimeField("date published", default=timezone.now())
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def was_posted_today(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.post_text[:20]
