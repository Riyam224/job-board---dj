from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    # every user has one profile 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # another fields  i want to add to user in the django page 
    city = models.ForeignKey("City", related_name='user_city', on_delete=models.CASCADE , null=True , blank=True)
    phone_number = models.CharField(_("phone number"), max_length=15)
    image = models.ImageField(_("image"), upload_to='profile')

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return str(self.user)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance , created ,   **kwargs):
    if created:
        Profile.objects.create(user=instance)

    


class City(models.Model):
    name = models.CharField(_("city"), max_length=50)

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Citys")

    def __str__(self):
        return self.name



