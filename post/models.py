from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django import forms
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_pic=models.ImageField(null=True, blank=True, upload_to="static/images/")
    read=models.IntegerField(null=True,blank=True)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category,default=1,on_delete=models.PROTECT)
    likes = models.ManyToManyField(User, null=True,blank=True,related_name='blog_post')
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('index')
