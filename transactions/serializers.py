from rest_framework import serializers
from generic_relations.relations import GenericRelatedField

from stocks.models import Stock
from stocks.serializers import StockSerializer
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    target = GenericRelatedField({
        Stock: StockSerializer(),
    })
    user = serializers.HyperlinkedRelatedField(read_only=True, view_name='accounts:account-detail')

    class Meta:
        model = Transaction
        fields = ('id', 'user', 'verb', 'created', 'target')
