from django.contrib import admin
from todoApp.models import Users, Task
# Register your models here.

admin.site.register([Users, Task])
