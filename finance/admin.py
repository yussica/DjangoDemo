# -*- coding: utf-8 -*-
from finance.models import FinanceItem
from django.contrib import admin

class FinanceItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['itemname']}),
        (None, {'fields':['costs']}),
        (None, {'fields':['detailinfo']}),
        ('日期', {'fields':['cost_date'], 'classes':['collapse']}),
    ]
    list_display = ('itemname', 'costs', 'detailinfo', 'cost_date')
    list_filter = ['cost_date']
    search_fields = ['itemname']
    date_hierarchy = 'cost_date'

admin.site.register(FinanceItem, FinanceItemAdmin)
