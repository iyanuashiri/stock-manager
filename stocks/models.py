from django.db import models
from django.urls import reverse

from accounts.models import Account

# Create your models here.


class StockManager(models.Manager):
    def buy_stock(self, owner, name, symbol, unit_price, shares, total_price):
        stock = self.create(owner=owner, name=name, symbol=symbol, unit_price=unit_price, shares=shares, total_price=total_price)
        return stock


class Stock(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='stocks')
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=50)
    unit_price = models.CharField(max_length=50)
    shares = models.CharField(max_length=50)
    total_price = models.CharField(max_length=50)
    bought_date = models.DateField(auto_now_add=True)

    objects = StockManager()

    class Meta:
        verbose_name = 'stock'
        verbose_name_plural = 'stocks'

    def __str__(self):
        return f'{self.symbol}'

    def get_absolute_url(self):
        return reverse('stocks:stock_detail', kwargs={'pk': self.pk})

    def sell(self, units):
        self.shares = self.shares - units
        self.save()
        return f'{self.shares} left'


class Search:
    def __init__(self, price, company_name):
        self.price = price
        self.company_name = company_name
