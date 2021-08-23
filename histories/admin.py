from django.contrib import admin
from .models import History


# Register your models here.

class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_time', 'transfer_amount', 'transfer_source', 'transfer_destination', 'account_amount']


admin.site.register(History, HistoryAdmin)
