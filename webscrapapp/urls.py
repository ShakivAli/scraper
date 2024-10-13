from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('food/', views.foodpage, name='food'),
    path('rest_submission/', views.restsubmission, name='rest_submission'),
    path('blockchain/', views.blockchainpage, name='blockchain'),
    path('blockchain_submission/', views.blockchainsubmission, name='blockchain_submission')
]
