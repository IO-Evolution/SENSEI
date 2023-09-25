import json

from PyCDArc.Components import ClinicalDocument as CD
from PyCDArc.Factory import XMLfactory as Factory
from PyCDArc.Templating.TemplateGenius import TemplateGenius, DOC_TYPE
from django.http import HttpResponse
from rest_framework.views import APIView

from .models import FSE_DOCUMENT_LOG
from .utils import get_client_ip


class ClinicalDocumentGeneration(APIView):

    def post(self, request):
        print(f"Incoming request from {get_client_ip(request)} for CDA generation service")
        try:
            doc = CD.ClinicalDocument("ClinicalDocument", request.data)
            fact = Factory.XMLfactory(doc)
            xml_str = fact.dict_to_xml()
            try:
                log = FSE_DOCUMENT_LOG(host=get_client_ip(request), json_code=request.data, xml_code=xml_str, doc_type=f"{request.data['code']['code']} {request.data['templateId']['extension']}", status="DONE")
            except:
                log = FSE_DOCUMENT_LOG(host=get_client_ip(request), json_code=request.data, xml_code=xml_str, doc_type="UNKNOWN", status="DONE")
            log.save()
            return HttpResponse(xml_str, content_type="application/xml", status=200)
        except Exception as e:
            try:
                log = FSE_DOCUMENT_LOG(host=get_client_ip(request), json_code=request.data, status="GENERATION_ERROR", doc_type=f"{request.data['code']['code']} {request.data['templateId']['extension']}", error=e)
            except:
                log = FSE_DOCUMENT_LOG(host=get_client_ip(request), json_code=request.data, status="GENERATION_ERROR", doc_type="UNKNOWN", error=e)
            finally:
                log.save()
                return_err = {
                    "ts": log.date.__str__(),
                    "error": log.error.__str__()
                }
                return HttpResponse(json.dumps(return_err), content_type="application/json", status=400)


class ClinicalDocumentTemplating(APIView):

    def get(self, request, doc_type):
        import json

        tg = TemplateGenius()
        json_doc = json.dumps(tg.generate_template(DOC_TYPE(doc_type)))
        return HttpResponse(json_doc, content_type="application/json")
