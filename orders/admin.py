from django.contrib import admin

from . import models

admin.site.register(models.Order)
admin.site.register(models.Projects)
admin.site.register(models.Setup)
