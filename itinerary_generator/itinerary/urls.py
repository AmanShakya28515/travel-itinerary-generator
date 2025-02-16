from django.urls import path 
from .import views 

urlpatterns = [
    path('create/', views.create_travel_plan, name='create_travel_plan'),  # This will map the URL to the view

   
]

