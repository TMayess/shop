from django.contrib.auth.models import AbstractUser
from django.db import models



class Adresse(models.Model):
    pays = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    codepostal = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.adresse}, {self.codepostal} {self.ville}, {self.pays}"




class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    adresse = models.OneToOneField(Adresse, on_delete=models.CASCADE, null=True, blank=True)
