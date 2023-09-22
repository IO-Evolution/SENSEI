from django.urls import path

from .views import GenerateDocument

urlpatterns = [
    path('generate/', GenerateDocument)
]
