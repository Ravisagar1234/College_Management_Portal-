from django.contrib import admin
from course.models import Course
from django.utils.html import format_html
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_title', 'image_tag', 'course_desc','duration','fees','eligibility']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.course_image.url))

    image_tag.short_description = 'Image'

admin.site.register(Course,CourseAdmin)