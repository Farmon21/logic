from django.contrib import admin
from django.contrib.auth.models import User

from authentication.models import FormData

# Register your models here.
admin.site.register(FormData)
