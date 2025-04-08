from django.urls import path
from .views import orm_list, checker


urlpatterns = [
    path('', orm_list, name='orm-list'),
    path('check', checker, name='check'),
    
]
