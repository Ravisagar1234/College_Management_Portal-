"""
URL configuration for Kitps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Kitps import views
from django.conf import settings
from django.conf.urls.static import static
from Kitps.views import course_list, course_detail

urlpatterns = [
    path('admin-kitps/', admin.site.urls),
    path('', views.HomePage,name="home"),
    path('search/', views.search, name='search'),
    path('aboutPage-kitps/', views.AboutPage,name="about"),
    path('ContactPage-kitps/', views.ContactPage,name="contact"),
    path('courses/', course_list, name='courses'),
    path('course/<int:id>/', course_detail, name='course_detail'),
    path('SaveInquiry-kitps/', views.saveInquiry,name="saveInquiry"),
    
    path('NewsPage-kitps/', views.NewsPage,name="news"),
    path('EventsPage-kitps/', views.EventsPage,name="events"),
    path('UserForm-kitps/', views.UserForm,name="form"),
    
    path('Calculator/',views.Calculator,name='Calculator'),
    path('evenodd/',views.evenodd),
    path('marksheet-kitps/',views.marksheet),
    path('NewsDetail-kitps/<slug:slugs>', views.newDetails, name='newsDetail')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    