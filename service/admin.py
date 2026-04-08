from django.contrib import admin
from service.models import Services


# Register your models here.



class CollegeEvent(admin.ModelAdmin):
    list_display=('service_image','service_heading','service_button' ,'service_desc')

   
admin.site.register(Services, CollegeEvent)    
