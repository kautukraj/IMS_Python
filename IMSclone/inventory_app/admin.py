from django.contrib import admin
from .models import *

# Register your models here.
# Documentation referred to : https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
# It reads data from models to provide a model-centric interface where trusted users can manage content

@admin.register (hatchback,sedan,SUVMUV,van) 
# register is given one or more model classes to register with the ModelAdmin
class ViewAdmin(admin.ModelAdmin):
    pass
