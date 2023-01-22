import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class TagManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Tag(models.Model):

    name = models.CharField(max_length=80, unique=True)
    objects = TagManager()

    def __str__(self):
        return self.name

    def natural_key(self):
        return "<" + self.name + ">"


class Post(models.Model):
    post_text = models.TextField(max_length=278)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    class Meta:
        unique_together = [["author", "post_text"]]

    def was_posted_today(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.post_text[:20]
