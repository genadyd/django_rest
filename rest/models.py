from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models


# 1 Category
# 2 Product
# 3 CardProduct
# 4 Card
# 5 Order
# **********
# 6 Customer
# 7 Specification

class Categories(models.Model):
    name = models.CharField(max_length=255, verbose_name="Category Name")
    description = models.TextField(verbose_name="Description")
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('rest.Categories', to_field='id', verbose_name='Parent', null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'


class Products(models.Model):
    category = models.ForeignKey(Categories, verbose_name="Category", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Product Name")
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name="Product Description", null=True)
    image = models.CharField(max_length=255, verbose_name="Product Picture", null=True)
    price = models.DecimalField(max_length=10, decimal_places=2, verbose_name="Price", max_digits=5)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'


class Customers(models.Model):
    name = models.CharField(max_length=255, verbose_name="Customer Name")
    email = models.EmailField(verbose_name="Customer Email")
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_date = models.DateTimeField(verbose_name="Registration Date")
    last_visit = models.DateTimeField(verbose_name="Last Visit")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'customers'


class Cards(models.Model):
    class CardStatus(models.TextChoices):
        NOT_PAYED = 'not_payed', _('not_py')
        APPROVED = 'approved', _('app')
        PENDING = 'pending', _('pen')

    customer = models.ForeignKey(Customers, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=100, choices=CardStatus.choices, default=CardStatus.NOT_PAYED)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'cards'


class CardProduct(models.Model):
    card = models.ForeignKey(Cards, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'cards_products'
