from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
# Create your models here.
class News(models.Model):
    news_title=models.CharField(max_length=100)
    news_description=HTMLField()
    news_image=models.FileField(upload_to="news/",max_length=300,null=True,blank=True)

    news_slugs = AutoSlugField(populate_from='news_title',unique=True,null=True,blank=True)