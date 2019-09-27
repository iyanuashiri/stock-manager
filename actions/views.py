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
        actions = Action.objects.filter(user=self.request.user)
        date = request.query_params.get('date', None)
        if date is not None:
            actions.filter(created=date)
        serializer = ActionSerializer(actions)
        return Response(serializer.data, status=status.HTTP_200_OK)
