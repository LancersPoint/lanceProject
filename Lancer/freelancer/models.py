from django.db import models
from django.conf import settings

class Gig(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='gigs_bidded',
                             on_delete=models.CASCADE)
    
    
