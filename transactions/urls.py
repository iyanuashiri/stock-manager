from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from transactions import views

app_name = 'transactions'
urlpatterns = [
    path('transactions/', views.TransactionList.as_view(), name='transaction-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
