from django.urls import path
from .views import orm_list


urlpatterns = [
    path('', orm_list, name='orm-list'),
    
]
