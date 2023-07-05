from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import FSE_DOCUMENT
from .serializers import DocumentSerializer

class DocumentApiView(APIView):
    def get(self, request, *args, **kwargs):
        documents = FSE_DOCUMENT.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)