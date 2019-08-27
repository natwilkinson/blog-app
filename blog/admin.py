from django.contrib import admin
from .models import Post # imports the Post model from models.py

admin.site.register(Post) # makes Model visible on admin page