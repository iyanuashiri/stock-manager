from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from actions import views


urlpatterns = [
    path('actions/', views.ActionList.as_view(), name='action-list'),
    path('actions/<date>/', views.ActionListByDate.as_view(), name='action-list-date'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
