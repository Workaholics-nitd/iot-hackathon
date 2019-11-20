from django.contrib import admin

from .models import Dustbin, Comment


# Register your models here.
admin.site.register(Dustbin)
admin.site.register(Comment)
