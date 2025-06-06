from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('blog/', views.blog, name='blog'),
]
