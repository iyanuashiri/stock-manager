from django.urls import path

from rest_framework.schemas import get_schema_view

from transactions import views

schema_view = get_schema_view(title='Transactions API')


app_name = 'transactions'
urlpatterns = [
    path('schema/', schema_view),

    path('transactions/', views.TransactionList.as_view(), name='transaction-list'),
]

