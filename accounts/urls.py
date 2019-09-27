from django.urls import path, include

from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='Accounts API')


app_name = 'accounts'
urlpatterns = [
    path('schema/', schema_view),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
