from django.urls import path

from apps.client import views

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('chart/', views.ChartsView.as_view(), name='index'),
]
