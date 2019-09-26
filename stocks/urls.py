from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from stocks import views


urlpatterns = [
    path('stocks/', views.StockList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
