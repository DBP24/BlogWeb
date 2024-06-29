from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name="Titulo")
    slug = models.SlugField(max_length=250, verbose_name="Slug URL")
    body = models.TextField(name="Cuerpo")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    # default Order
    class Meta():
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]

    # return object default   
    def __str__(self):
        return self.title
    




# class Post(models.Model):
#  title = models.CharField(max_length=250)
#  slug = models.SlugField(max_length=250)
#  body = models.TextField()
#  def __str__(self):
#  return self.title