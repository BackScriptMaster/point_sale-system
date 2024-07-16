from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales_index, name="sales_index")
]

