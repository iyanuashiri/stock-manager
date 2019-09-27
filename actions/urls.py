from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from actions import views


urlpatterns = [
    path('actions/', views.ActionList.as_view(), name='action-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
