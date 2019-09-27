from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from transactions import views

app_name = 'actions'
urlpatterns = [
    path('actions/', views.TransactionList.as_view(), name='action-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
