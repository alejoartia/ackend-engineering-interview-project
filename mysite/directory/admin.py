from django.contrib import admin
from .models import Company, User
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.

admin.site.register(User)
admin.site.register(Company)



TokenAdmin.raw_id_fields = ['user']