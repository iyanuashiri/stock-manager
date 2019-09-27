import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Action
from .serializers import ActionSerializer

# Create your views here.


class ActionList(APIView):
    """

    """
    def get(self, request, *args, **kwargs):
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)
        if start_date and end_date is not None:
            actions = Action.objects.filter(user=self.request.user, created__range=(Action.parse_date(start_date), Action.parse_date(end_date)))
        else:
            actions = Action.objects.filter(user=self.request.user)
        serializer = ActionSerializer(actions)
        return Response(serializer.data, status=status.HTTP_200_OK)
