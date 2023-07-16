from django.db import models

# Create your models here.
from django.urls import reverse

"""
Product
- Libelle
- Prix
- Description
- Taille
- Couleur 
- image
- matiere
"""

class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    material = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product)
