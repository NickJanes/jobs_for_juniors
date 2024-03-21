from django.urls import path, include
from . import views

urlpatterns = [    
  path('profile/', views.profile, name='profile'),
  path('profile/edit/', views.edit_profile, name='edit_profile'),
  path('profile/resumes/', views.resumes, name='resumes'),
  path('profile/postings/', views.postings, name='postings'),
  path("register/<str:role>/", views.register, name='register'),
  path("", include("django.contrib.auth.urls")),
]
