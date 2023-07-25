from django.urls import path
from . import views
urlpatterns = [
    path('registerUser/', views.resgisterUser, name='resgisterUser')
]