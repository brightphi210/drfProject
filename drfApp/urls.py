from django.urls import path
from .views import *

urlpatterns = [
    path('', GetPostTodo.as_view(),  name=''),
    path('update/<str:pk>/', UpdateDeleteTodo.as_view(),  name='')
]