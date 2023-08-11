from PyCDA.Factory import XMLfactory as Factory
from PyCDA.Components import ClinicalDocument as CD

from rest_framework.views import APIView
from django.http import HttpResponse

class ClinicalDocumentGeneration(APIView):

    def post(self, request, format=None):
        doc = CD.ClinicalDocument("ClinicalDocument", request.data)
        fact = Factory.XMLfactory(doc)
        return HttpResponse(fact.dict_to_xml(), content_type="application/xml")