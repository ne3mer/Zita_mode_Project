from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class AboutMe(models.Model):
    image = models.ImageField(upload_to='images/about/%Y/%m/%d', null=True, verbose_name='تصویر اصلی',
                              default='')

    body = body = RichTextField(default='',verbose_name='متن درباره ما')

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'
