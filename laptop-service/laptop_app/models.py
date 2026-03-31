from django.db import models


class Laptop(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, default='')
    cpu = models.CharField(max_length=100, blank=True, default='')
    ram = models.CharField(max_length=50, blank=True, default='')
    storage = models.CharField(max_length=100, blank=True, default='')
    screen_size = models.CharField(max_length=50, blank=True, default='')
    stock = models.PositiveIntegerField(default=0)
    image_url = models.URLField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.name}"

    class Meta:
        ordering = ['-created_at']
