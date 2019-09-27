from rest_framework import serializers

from .models import Action


class ActionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedRelatedField(read_only=True, view_name='actions:action-detail')
    user = serializers.HyperlinkedRelatedField(read_only=True, view_name='accounts:account-detail')

    class Meta:
        model = Action
        fields = ('id', 'url', 'user', 'verb', 'created', 'target_ct', 'target_id', 'target')
