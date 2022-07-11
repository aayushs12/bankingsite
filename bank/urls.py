from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.index,name='home'),
    path('', views.index, name='index'),
    path('transaction/',views.transaction,name='transaction'),
]
