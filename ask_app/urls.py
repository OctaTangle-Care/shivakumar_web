
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.footer, name='footer'),
    # path('', views.header, name='header'),
    path('contact', views.contact, name='contact'),
    path('skill', views.skill, name='skill'),
    path('gallery', views.gallery, name='gallery'),
    path('projects', views.project, name='project'),
    path('about', views.about, name='about'),
    path('home', views.home, name='home'),
    path('', views.intro, name='intro'),
    path('privacy', views.privacy, name='privacy'),
    path('contactus/',views.contactus,name="contactus"),
    path('update/',views.update,name="update"),
    
    

]
