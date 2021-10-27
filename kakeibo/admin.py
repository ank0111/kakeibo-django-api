from django.contrib import admin
from .models import *
# Register your models here.
list(map(admin.site.register, [ICategory, OCategory, Store, Income, Outgo]))
