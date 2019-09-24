from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from . import viewsets


schema_view = get_schema_view(title='Accounts API')

router = DefaultRouter()
router.register(r'accounts', viewsets.AccountViewset)


app_name = 'accounts'
urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
