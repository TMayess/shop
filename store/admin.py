from django.contrib import admin

from store.models import Product, ProductImage, Category, Color, Stock

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Stock)