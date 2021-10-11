from django.contrib import admin
from .models import Order_item


class OrderAdmin(admin.ModelAdmin):
    list_display=['id','customer','laptop','price','quantity']
admin.site.register(Order_item,OrderAdmin)
