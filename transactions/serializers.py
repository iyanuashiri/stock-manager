from rest_framework import serializers
from generic_relations.relations import GenericRelatedField

from stocks.models import Stock
from stocks.serializers import StockSerializer
from .models import Transaction


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    target = GenericRelatedField({
        Stock: StockSerializer(),
    })
    url = serializers.HyperlinkedRelatedField(read_only=True, view_name='transactions:transaction-detail')
    user = serializers.HyperlinkedRelatedField(read_only=True, view_name='accounts:account-detail')

    class Meta:
        model = Transaction
        fields = ('id', 'url', 'user', 'verb', 'created',  'target')
