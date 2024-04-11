from django.contrib import admin

from communityapp.models import DriverLoginDetails, requestitem

# Register your models here.
admin.site.register(requestitem)
admin.site.register(DriverLoginDetails)