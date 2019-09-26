from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from stocks import views


urlpatterns = [
    path('stocks/', views.StockList.as_view(), name='stock-list'),
    path('stocks/<symbol>/buy/<shares>/', views.StockBuy.as_view(), name='stock-buy'),
    path('stocks/<symbol>/sell/<shares>/', views.StockSell.as_view(), name='stock-sell'),
    path('stocks/<symbol>/search/', views.StockSearch.as_view(), name='stock-search'),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
