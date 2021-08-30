from django.contrib import admin

from .models import Bank


# Register your models here.

class BankAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Bank, BankAdmin)
