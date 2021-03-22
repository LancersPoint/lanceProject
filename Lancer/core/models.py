from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


#TODO: CREATE TAGS TO REPRESENTS THE SKILLS FOR AN EMPLOYEE TO CHOSE REQUIRED SKILLS FOR THE JOB

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class JobPost(models.Model):
    """Model for the job posted by the employer"""
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )

    objects = models.Manager()  # the default manager
    # TODO: ADD TAGS
    published = PublishedManager()  # to easilyy retrieve published posts
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


class Bid(models.Model):
    """Model to hold the information of the people bidding for a job"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='bidders',
                             on_delete=models.CASCADE)
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)


class Gig(models.model):
    """Model for the confirmed job to a freelancer"""
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='freelancer',
                             on_delete=models.CASCADE)
    employer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 related_name='employer',
                                 on_delete=models.CASCADE)
    job_assigned = models.ManyToManyField(Bid)
    


# class Gig(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              related_name='bidders',
#                              on_delete=models.CASCADE)
#     bid = models.ManyToManyField(JobPost, blank=True, related_name="bids")
