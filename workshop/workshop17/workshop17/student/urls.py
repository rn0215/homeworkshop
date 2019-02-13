from django.urls import path
from . import views

urlpatterns = [
    path("", views.student),    
    path("person/<str:name>",views.person)
]