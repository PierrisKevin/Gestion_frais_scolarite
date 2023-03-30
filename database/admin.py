from django.contrib import admin
from .models import student, paiment, administrator

admin.site.register(student)
admin.site.register(paiment)
admin.site.register(administrator)