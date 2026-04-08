from django.db import models

# Create your models here.
class Course(models.Model):
    course_title=models.CharField(max_length=50)
    course_image=models.ImageField(upload_to='courses')
    course_desc =models.CharField(max_length=250)

     # NEW fields (optional but recommended)
    duration    = models.CharField(max_length=50, blank=True, null=True)
    fees        = models.CharField(max_length=50, blank=True, null=True)
    eligibility = models.CharField(max_length=200, blank=True, null=True)