from django.urls import path

from .views import ClinicalDocumentGeneration

urlpatterns = [
     path('generate/', ClinicalDocumentGeneration.as_view())
]
