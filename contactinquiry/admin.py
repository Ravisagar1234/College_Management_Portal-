from django.contrib import admin
from contactinquiry.models import ContactInquiry
# Register your models here.

class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone','course','qualification','city','message','created_at']

admin.site.register(ContactInquiry, ContactInquiryAdmin)