from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.index, name='search'),
    path('apply/<int:posting_id>', views.apply, name='apply'),
    path('posting/<int:posting_id>', views.posting, name='posting-detailed'),
    path('create_posting_form', views.create_posting, name='create_posting'),
]
