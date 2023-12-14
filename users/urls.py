from django.urls import path, include
from . import views

urlpatterns = [    
  path('profile/', views.profile, name='profile'),
  path("register/<str:role>", views.register, name='register'),
  path("", include("django.contrib.auth.urls")),
]
