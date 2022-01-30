from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Info(models.Model):
    place = models.CharField(_("place"), max_length=50)
    phone = models.CharField(_("phone number"), max_length=20)
    email = models.EmailField(_("email"), max_length=254)

    

    class Meta:
        verbose_name = _("Info")
        verbose_name_plural = _("Infos")

    def __str__(self):
        return self.email

