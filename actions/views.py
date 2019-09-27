from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions

from .models import Action
from .serializers import ActionSerializer

# Create your views here.


class ActionList(generics.ListAPIView):
    """

    """
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        actions = self.queryset.filter(user=self.request.user)
        return actions


class ActionListByDate(APIView):
    """

    """
    def get(self, request, date=None, format=None):
        actions = Action.objects.filter(user=self.request.user, created=date)
        serializer = ActionSerializer(actions)
        return Response(serializer.data)
