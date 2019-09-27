import datetime

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone

# Create your models here.


class Action(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='actions', db_index=True)
    verb = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True, db_index=True)
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_obj', on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.target_ct} {self.verb}'

    @staticmethod
    def create_action(user, verb, target=None):
        now = timezone.now()
        last_date = now - datetime.timedelta(seconds=60)
        similar_actions = Action.objects.filter(user_id=user.id, verb=verb, created_gte=last_date)

        if target:
            target_ct = ContentType.objects.get_for_model(target)
            similar_actions = similar_actions.filter(target_ct=target_ct, target_id=target.id)

        if not similar_actions:
            action = Action.objects.create(user=user, verb=verb, target=target)
            return True
        return False
