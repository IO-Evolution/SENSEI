from django.urls import path

from .views import ClinicalDocumentGeneration, ClinicalDocumentTemplating

urlpatterns = [
    path('generate/', ClinicalDocumentGeneration.as_view()),
    path('templating/<int:doc_type>', ClinicalDocumentTemplating.as_view()),
]
