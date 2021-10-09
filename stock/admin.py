from django.contrib import admin

from stock.models import Stock
from stock.models import Currency

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin) :
    list_display = ("ticker", "name", "description")
    pass

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass