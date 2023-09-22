import json
from PyCDA.Factory import XMLfactory as Factory
from PyCDA.Components import ClinicalDocument as CD

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def GenerateDocument(self, request):
    json_data = json.load(request.data.get('document'))
    doc = CD.ClinicalDocument("ClinicalDocument", json_data["ClinicalDocument"])
    fact = Factory.XMLfactory(doc)
    return Response({"ClinicalDocument": fact.dict_to_xml()}, status=status.HTTP_200_OK)
