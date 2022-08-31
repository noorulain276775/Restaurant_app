from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group


admin.site.unregister(Group)
admin.site.site_header = "Noor's Restaurant"
admin.site.site_title = "Food"
admin.site.index_title = "What do you want to eat?"


class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ('email',)
admin.site.register(Customer, CustomerAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'price')

    def price(self, obj):
        p = obj.item.price*obj.quantity
        return p


admin.site.register(Cart, OrderItemAdmin)



class ItemAdmin(admin.ModelAdmin):
    list_display = ('image', 'item_type', 'name', 'description', 'price')
    list_display_links = ('item_type', 'name' )
admin.site.register(Item, ItemAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_order_items', 'customer', 'address',
                    'created_at', 'status')
    list_display_links = ['get_order_items', 'customer']
    # filter_horizontal = ['order_item']
    def get_order_items(self, obj):
        order = obj.order_item.item.name
        return order
        
admin.site.register(Order, OrderAdmin)
