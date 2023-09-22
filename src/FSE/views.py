from PyClinicalDocumentArchitecture.Components import ClinicalDocument as CD
from PyClinicalDocumentArchitecture.Factory import XMLfactory as Factory
from django.http import HttpResponse
from rest_framework.views import APIView


class ClinicalDocumentGeneration(APIView):

    def post(self, request, format=None):
        doc = CD.ClinicalDocument("ClinicalDocument", request.data)
        fact = Factory.XMLfactory(doc)
        return HttpResponse(fact.dict_to_xml(), content_type="application/xml")


class ClinicalDocumentTemplate(APIView):

    def get(self, request, doc_type):
        from PyClinicalDocumentArchitecture.Templating.TemplateGenius import TemplateGenius, DOC_TYPE
        import json
        tg = TemplateGenius()
        json_doc = json.dumps(tg.generate_template(DOC_TYPE(doc_type)))
        return HttpResponse(json_doc, content_type="application/json")
