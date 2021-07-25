from django.urls import path
from . import views

urlpatterns = [
   path('create/<str:place>', views.create_place)
]
