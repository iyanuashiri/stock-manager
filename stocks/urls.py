from django.urls import path

from rest_framework.schemas import get_schema_view

from stocks import views


schema_view = get_schema_view(title='Stocks API')


app_name = 'stocks'
urlpatterns = [
    path('schema/', schema_view),

    path('stocks/', views.StockList.as_view(), name='stock-list'),
    path('stocks/<symbol>/buy/<int:shares>/', views.StockBuy.as_view(), name='stock-buy'),
    path('stocks/<symbol>/sell/<int:shares>/', views.StockSell.as_view(), name='stock-sell'),
    path('stocks/<symbol>/search/', views.StockSearch.as_view(), name='stock-search'),
]

