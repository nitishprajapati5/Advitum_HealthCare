from django.urls import path
from .views import home,first

urlpatterns = [
    path('', first, name='first'),
    path('home.html', home, name='home'),
  
]
