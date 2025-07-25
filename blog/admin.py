# blog/admin.py
from django.contrib import admin
from .models import Post

# Admin panelga Post modelini qo‘shamiz
admin.site.register(Post)
