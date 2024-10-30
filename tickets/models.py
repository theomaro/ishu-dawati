from django.db import models

# Create your models here.


class Centre(models.Model):
    number = models.CharField(max_length=254, unique=True, primary_key=True)
    name = models.CharField(max_length=254)
    region = models.CharField(max_length=254)
    district = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=245, unique=True)

    class Meta:
        unique_together = ["number", "name"]
        ordering = ["name", "number"]

    def __str__(self):
        return f"{self.number} - {self.name}"
