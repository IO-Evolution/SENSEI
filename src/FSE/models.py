from django.db import models

# DATA
DOCS_CHOICES = (
    ('LDO','Lettera di Dimissione Ospedaliera'),
    ('CERT_VACC', 'Certificato Vaccinale'),
    ('SING_VACC','Singola Vaccinazione'),
)

DOCS_STATUS = (
    ('DONE','Completato'),
    ('GENERATION_ERROR', 'Errore nella Generazione'),
    ('VALIDATION_ERROR', 'Errore nella Validazione'),
    ('SUBMISSION_ERROR', 'Errore nella Sottomissione'),
    ('WAIT','In attesa di Sottomissione'),
)

class FSE_DOCUMENT(models.Model):

    id = models.AutoField("ID", primary_key=True)
    doc_type = models.CharField("Document Type", max_length=50, choices=DOCS_CHOICES)
    xml_file = models.FileField("XML", upload_to="FSE/storage", blank=True, null=True)
    xml_code = models.TextField("Code", blank=True, null=True)
    data = models.DateTimeField("Timestamp", auto_now=True, auto_now_add=False)
    status = models.CharField("Status", max_length=50, choices=DOCS_STATUS)
    
    def save(self, *args, **kwargs):
        super(FSE_DOCUMENT, self).save(*args, **kwargs)
        file = open(self.xml_file.path, "r")
        self.xml_code = file.read()
        file.close()
        super(FSE_DOCUMENT, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "DOCUMENT"
        verbose_name_plural = "DOCUMENTS"

    def __str__(self):
        return str(self.id) + " - " + self.doc_type

    # def get_absolute_url(self):
    #     return reverse("FSE_DOCUMENT_detail", kwargs={"pk": self.pk})
