from django.urls import path

from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns

from transactions import views

schema_view = get_schema_view(title='Transactions API')


app_name = 'transactions'
urlpatterns = [
    path('schema/', schema_view),

    path('transactions/', views.TransactionList.as_view(), name='transaction-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
