from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.index, name='search'),
    path('posting/<int:posting_id>', views.posting, name='posting'),
    path('create_posting_form', views.create_posting_form, name='create_posting_form'),
    path('create_posting_action', views.create_posting_action, name='create_posting_action'),
    path('profile/', views.profile, name='profile'),
    path("accounts/register/", views.register, name='register'),
    path("accounts/", include("django.contrib.auth.urls")),
]
