from django.contrib import admin

from apps.product.models import Product, ProductVariant, Category, CartItem, Cart, OrderItem, Order

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
