from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

from eiser_shop.models import Product


class Card(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE, related_name='my_card')
    products = models.ManyToManyField(Product, related_name='products_cards')
    # Добавьте другие поля, связанные с корзиной


class User(AbstractUser):
    # Ваша модель User
    name = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=20)
    repeatpassword = models.CharField(max_length=20)
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='card_users_shop')
    card = models.OneToOneField(Card, on_delete=models.CASCADE, null=True, related_name='user_card')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='eiser_shop_users',
        help_text='Specific permissions for the user.',
        related_query_name='eiser_shop_user',
    )

    def __str__(self):
        return f"Cart for {self.user.name}"

