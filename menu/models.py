from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import userCreationManager



class Item(models.Model):
    TYPE = [('REGULAR', 'Regular'), ('SPICY', 'Spicy')]
    item_type = models.CharField(max_length=7, choices=TYPE)
    image = models.ImageField(upload_to="menu")
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=500)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}"


class Customer(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects= userCreationManager()

    def __str__(self):
        return f"{self.email}"

class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        ordering = ('-item',)


    def __str__(self):
        return f"{self.item.name}- {self.item.price}"
    
    @property
    def get_item_cost(self):
        item_cost = self.item.price*self.quantity
        return item_cost


class Order(models.Model):
    STATUS = [('In-Process', 'Processing'), ('Order Delievered', 'Completed')]
    order_item = models.ForeignKey(Cart, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default="In-Process", max_length=16, choices=STATUS, blank=True)
    completed = models.BooleanField(default=False, blank=True)


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.order_item} {self.customer.email}"

