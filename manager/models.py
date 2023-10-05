from django.db import models

from django.db.models import QuerySet

from django.urls import reverse

from django.utils import timezone

from django.contrib.auth.models import User


class PublishedManager(models.Manager):

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Content.Status.PUBLISHED)
    

class Content(models.Model):


    class Status(models.TextChoices):

        DRAFT = 'DF','DRAFT'
        PUBLISHED = 'PB','PUBLISHED'




    title = models.CharField(max_length=250)

    slug = models.SlugField(max_length=250,unique_for_date='publish')

    body = models.TextField()

    author = models.ForeignKey(User,on_delete=models.CASCADE,
                               related_name='content_posts',null=True)

    image = models.ImageField(upload_to='media/content')

    publish = models.DateTimeField(timezone.now)

    status = models.CharField(max_length=2,choices=Status.choices,
                              default=Status.DRAFT)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    published = PublishedManager()

    objects = models.Manager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('content:detail_services',args=[self.publish.year,
                                               self.publish.month,
                                               self.publish.day,
                                               self.slug])
        


class Comment(models.Model):

    content = models.ForeignKey(Content,on_delete=models.CASCADE,
                                related_name='comments')
    
    name = models.CharField(max_length=85)

    body = models.TextField()

    email = models.EmailField()

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self) -> str:
        return f"comment {self.name} or {self.content}"