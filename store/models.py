from django.db import models

# Create your models here.
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
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    material = models.CharField(max_length=128)

    def __self__(self):
        return f"{self.name}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __self__(self):
        return f"{self.product}"
