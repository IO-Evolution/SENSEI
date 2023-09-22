from django.urls import path
from .views import ClinicalDocumentGeneration, ClinicalDocumentTemplate

urlpatterns = [
     path('generate/', ClinicalDocumentGeneration.as_view()),
     path('template/<int:doc_type>', ClinicalDocumentTemplate.as_view())
]
