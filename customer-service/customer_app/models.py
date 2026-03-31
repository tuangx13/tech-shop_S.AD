from django.db import models


class Cart(models.Model):
    # Use simple user_id instead of ForeignKey since users are in auth-service
    user_id = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of user {self.user_id}"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())


class CartItem(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ("laptop", "Laptop"),
        ("mobile", "Mobile"),
    ]

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product_id = models.IntegerField()
    product_type = models.CharField(max_length=10, choices=PRODUCT_TYPE_CHOICES)
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("cart", "product_id", "product_type")

    def __str__(self):
        return f"{self.product_name} x{self.quantity}"

    @property
    def total_price(self):
        return self.product_price * self.quantity
