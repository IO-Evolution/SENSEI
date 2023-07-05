from django.urls import path

from .views import DocumentApiView

urlpatterns = [
    path('list/all', DocumentApiView.as_view()),
]
