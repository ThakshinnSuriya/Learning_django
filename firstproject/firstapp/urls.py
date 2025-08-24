from django.urls import path
from . import views

urlpatterns = [
    path('class',views.hello.as_view(), name='hello_class'),
    path('function', views.hello_world, name='hello_function'),
    path('reservation', views.home),
]