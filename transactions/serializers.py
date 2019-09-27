from rest_framework import serializers

from .models import Transaction


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedRelatedField(read_only=True, view_name='transactions:transaction-detail')
    user = serializers.HyperlinkedRelatedField(read_only=True, view_name='accounts:account-detail')

    class Meta:
        model = Transaction
        fields = ('id', 'url', 'user', 'verb', 'created', 'target_ct', 'target_id', 'target')
