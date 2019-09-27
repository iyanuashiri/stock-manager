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
