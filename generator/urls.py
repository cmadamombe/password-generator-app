from generator import views
from django.urls import path

# app level urls
app_name = "generator"

urlpatterns = [
    path('generator/', views.password, name='password'),
]