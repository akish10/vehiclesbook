from django.contrib import admin

# Register your models here.
from .models import Vehicle , Payment

admin.site.register(Vehicle)
admin.site.register(Payment)