from django.contrib import admin
from .models import Account


# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'amount', 'created_time', 'bank', 'modified_time']


admin.site.register(Account, AccountAdmin)
