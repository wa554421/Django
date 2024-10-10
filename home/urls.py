from django.contrib import admin
from django.urls import path,include
from webcolors import names

admin.site.site_header = "Waleed Admin"
admin.site.site_title = "Mart Admin Portal"
admin.site.index_title = "Welcome to Mysteric Mart Portal"

from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('contact',views.contact,name="contact")
]
