from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ContactInquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField()

    COURSE_CHOICES = [
        ('CSE', 'B.Tech (CSE)'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('EE', 'Electrical Engineering'),
    ]

    course = models.CharField(max_length=50,choices=COURSE_CHOICES,blank=True,null=True)
    qualification = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=200,blank=True,null=True)
    message = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 🔥 timestamp

    def __str__(self):
        return self.name