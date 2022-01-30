from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth.models import User
JOB_TYPE = (
    ('Full Time' , 'Full Time'),
    ('Part Time' , 'Part Time')
)


class Job(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=50)
    # location
    job_type = models.CharField(_("job_type"), max_length=50 , choices=JOB_TYPE)
    description = models.TextField(_("description"))
    published_at = models.DateTimeField(_("published at "), auto_now=True)
    vacancy = models.IntegerField(_("vacancy") , default=1)
    salary   = models.IntegerField(_("salary") , default=9)
    experience = models.IntegerField(_("experience") , default=1)
    category = models.ForeignKey('Category',  on_delete=models.CASCADE)
    image = models.ImageField(_("images"), upload_to='job')
    slug = models.SlugField(_("slug") , null=True , blank=True)
 
    
 
    class Meta:
        verbose_name = _("Job")
        verbose_name_plural = _("Jobs")

    def __str__(self):
        return self.title

    
    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Job , self).save(*args, **kwargs)
  

class Category(models.Model):

    name = models.CharField(_("name"), max_length=50)
  
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
  
    def __str__(self):
        return self.name
  


class Apply(models.Model):
    job = models.ForeignKey(Job, verbose_name=_("job"), on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=50)
    email = models.EmailField(_("email"), max_length=254)
    website = models.URLField(_("website"), max_length=200)
    cv = models.FileField(_("cv"), upload_to='apply', max_length=100)
    cover_letter = models.TextField(_("cover letter"))
    created_at = models.DateTimeField(_("created at "), auto_now=True)


    class Meta:
        verbose_name = _("Apply")
        verbose_name_plural = _("Applies")

    def __str__(self):
        return str(self.name)

  

