from django.urls import path

from api import views

urlpatterns = [
    path('v1/', views.api_home),
]
