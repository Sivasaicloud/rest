from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.URLField(max_length=2000, blank=True)

    def __str__(self):
        return self.name
