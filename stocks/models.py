from django.db import models
from django.urls import reverse

from accounts.models import Account

# Create your models here.


class Stock(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='stocks')
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=50)
    unit_price = models.CharField()
    units = models.IntegerField()
    total_price = models.CharField()

    class Meta:
        verbose_name = 'stock'
        verbose_name_plural = 'stocks'

    def __str__(self):
        return f'{self.symbol}'

    def get_absolute_url(self):
        return reverse('stocks:stock_detail', kwargs={'pk': self.pk})
