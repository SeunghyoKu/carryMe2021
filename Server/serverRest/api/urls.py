from django.urls import path, include
from .views import helloApi
from .views import exampleAPI

urlpatterns = [
    path("hello/", helloApi),
    path("example/", exampleAPI)
]
