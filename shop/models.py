from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.utils.text import slugify
=======
>>>>>>> 7e0d1c97e8ab9933dbec51a67900c5671ea590fd

# --------------------------
# Product Model
# --------------------------
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
<<<<<<< HEAD
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
=======
>>>>>>> 7e0d1c97e8ab9933dbec51a67900c5671ea590fd
    created_at = models.DateTimeField(auto_now_add=True)  # for admin list_display

    def __str__(self):
        return self.name

<<<<<<< HEAD
    def save(self, *args, **kwargs):
        # Auto-generate a slug from the name if not provided
        if not self.slug:
            base = slugify(self.name)[:200]
            slug = base
            # Ensure uniqueness
            counter = 1
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

=======
>>>>>>> 7e0d1c97e8ab9933dbec51a67900c5671ea590fd

# --------------------------
# Order Model
# --------------------------
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # add this
    ordered_at = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
    # Payment fields
    # Only Cash on Delivery is supported now
    PAYMENT_CHOICES = [
        ('cod', 'Cash on Delivery'),
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='cod')
    is_paid = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=200, blank=True, null=True)
=======
>>>>>>> 7e0d1c97e8ab9933dbec51a67900c5671ea590fd

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
