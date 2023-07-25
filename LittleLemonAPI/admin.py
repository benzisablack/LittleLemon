from django.contrib import admin
from LittleLemonAPI.models import Order, MenuItem, Category, OrderItem, Cart

# Register your models here.
admin.site.register(Order)
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(Cart)
