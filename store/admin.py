from django.contrib import admin

from store.models import Product,ProductImage

admin.site.register(Product)
admin.site.register(ProductImage)