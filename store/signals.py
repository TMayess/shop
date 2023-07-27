from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Stock


@receiver(post_save, sender=Stock)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:

        product = instance.product
        stocks_for_product = Stock.objects.filter(product=product)
        quantity = sum(stock.quantity for stock in stocks_for_product)
        product.quantity = quantity
        product.save()