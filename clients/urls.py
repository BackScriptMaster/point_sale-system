from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_index, name="clients_index")
]

