from django.urls import path
from .views import *


urlpatterns = [
    path('', myapp_view, name='hello'),
    path('second/', second_page, name="second"),
    path('pages/<str:page>', pages, name='pages'),
]
