from django.db import models
from django.contrib.auth.models import User

# --------------------------
# Product Model
# --------------------------
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # for admin list_display

    def __str__(self):
        return self.name


# --------------------------
# Order Model
# --------------------------
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # add this
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


# --------------------------
# OrderItem Model
# --------------------------
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def total_price(self):
        return self.quantity * self.product.price
