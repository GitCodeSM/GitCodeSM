from django.contrib import admin

# Register your models here.
from .models import MyUser, Plans

admin.site.register(MyUser)
admin.site.register(Plans)
