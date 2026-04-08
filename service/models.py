from django.db import models

# Create your models here.


class Services(models.Model):
    service_image  =models.CharField(max_length=50)
    service_heading=models.CharField(max_length=50)
    service_button =models.CharField(max_length=50)
    service_desc   =models.TextField()    