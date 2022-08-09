from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey("accounts.User", default=1, on_delete=models.CASCADE)
    tag_set=models.ManyToManyField("Tag",blank=True)

    def get_absolute_url(self):
        return reverse("blog:post", args=[self.pk])

    def __str__(self):
        return self.title


class Tag(models.Model):
    name=models.CharField(max_length=80,unique=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)
    post=models.ForeignKey("Post",blank=True, on_delete=models.CASCADE)
    content=models.TextField()

    def __str__(self):
        return self.content