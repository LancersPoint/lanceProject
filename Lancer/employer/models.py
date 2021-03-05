from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


#TODO: CREATE TAGS TO REPRESENTS THE SKILLS FOR AN EMPLOYEE TO CHOSE REQUIRED SKILLS FOR THE JOB

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')
class Posts(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )

    objects = models.Manager() # the default manager
    published = PublishedManager() # to easilyy retrieve published posts
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    employer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='jobs_posted')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

    #Todo: add a conical url. Absolute url to see details about a post
    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title


class Bidders(models.Model):
    post = models.ForeignKey(
        Posts, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()
    from_who = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        related_name='sender',
                                        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Message by {self.from_who} on {self.post}'
