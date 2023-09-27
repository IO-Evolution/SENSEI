from django.db import models

# DATA
DOCS_CHOICES = (
    ('34105-7 1.2', 'Lettera di Dimissione Ospedaliera'),
    ('CERT_VACC', 'Certificato Vaccinale'),
    ('SING_VACC', 'Singola Vaccinazione'),
    ('RSA', 'RSA'),
    ('UNKNOWN', 'Non presente')
)

DOCS_STATUS = (
    ('DONE', 'Completato'),
    ('GENERATION_ERROR', 'Errore nella Generazione')
)


class FSE_DOCUMENT_LOG(models.Model):
    id = models.AutoField("ID", primary_key=True)
    host = models.CharField("HOST", max_length=15, blank=False, null=False)
    doc_id = models.CharField("Document ID", max_length=500, blank=True, null=True)
    doc_type = models.CharField("Document Type", max_length=50, choices=DOCS_CHOICES)
    xml_code = models.TextField("XML Code", blank=True, null=True)
    json_code = models.TextField("JS Code", blank=True, null=True)
    error = models.TextField("Error", blank=True, null=True)
    date = models.DateTimeField("Timestamp", auto_now=True, auto_now_add=False)
    status = models.CharField("Status", max_length=50, choices=DOCS_STATUS)
    note = models.TextField("Note", blank=True, null=True)

    class Meta:
        verbose_name = "DOCUMENT"
        verbose_name_plural = "DOCUMENTS"

    def __str__(self):
        return str(self.id) + " - " + self.date.__str__()
