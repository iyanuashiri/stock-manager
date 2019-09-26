from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from stocks import views


urlpatterns = [
    path('stocks/', views.StockList.as_view()),
    path('stocks/<symbol>/buy/<shares>/', views.StockBuy.as_view()),
    path('stocks/<symbol>/sell/<shares>/', views.StockSell.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
