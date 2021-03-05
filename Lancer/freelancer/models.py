from django.db import models
from django.conf import settings
from employer.models import Posts

class Gig(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='bidders',
                             on_delete=models.CASCADE)
    bid = models.ManyToManyField(Posts, blank=True, related_name="bids")
    
    
