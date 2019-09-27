from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Administrator,Staff,Applicant,RefactoryUser


# Register your models here.

admin.site.register(RefactoryUser)

admin.site.register(Administrator)

admin.site.register(Staff)

admin.site.register(Applicant)

