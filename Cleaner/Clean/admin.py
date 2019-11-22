from django.contrib import admin
from .models import Donation,Category,Institution

# Register your models here.

admin.site.register(Donation)
admin.site.register(Institution)
admin.site.register(Category)
