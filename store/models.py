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


class Category(models.Model):
    GENDER_CHOICES = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('U', 'Unisexe'),
    )

    name = models.CharField(max_length=30)
    sexe = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    material = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return str(self.product)


class Color(models.Model):
    colorHexadecimal = models.CharField(max_length=7)

    def __str__(self):
        return self.colorHexadecimal


class Size(models.Model):
    SIZE_CHOICES = (
        ('m', 'Medium'),
        ('s', 'Small'),
        ('x', 'Extra Small'),
        ('xl', 'Extra Large'),
        ('xxl', 'Extra Extra Large'),
    )

    name = models.CharField(max_length=3, choices=SIZE_CHOICES, unique=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product} - {self.color} - {self.size}"
