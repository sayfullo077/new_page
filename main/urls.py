from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home'),
]
