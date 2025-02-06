from django.urls import path
from . import views


urlpatterns = [
    path("classify-number/",views.class_number, name="classify-number")
]