from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from pkg_resources import require
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from cities import 



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    signup_confirmation = models.BooleanField(default=False)
    country = CountryField(null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    resume = models.FileField(upload_to='documents/', blank=True)
    phone_number = PhoneNumberField(null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField()
    title = models.CharField(max_length=300)
    send_mail = models.BooleanField(default=True)

    # TODO: Address 
    # TODO: CITY 
    # TODO: SKILLS  THINK SHOULD BE ANOTHER MODEL IN ITS OWN?

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)



# @receiver(post_save, sender=User)
# def update_profile_signal(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()