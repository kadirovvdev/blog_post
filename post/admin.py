from django.contrib import admin
from django.urls import path, include
from .models import *




# Register your models here.


admin.site.register(Post)
admin.site.register(Review)
