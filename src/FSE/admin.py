from django.contrib import admin
from django.utils.html import format_html
from .models import FSE_DOCUMENT_LOG


@admin.register(FSE_DOCUMENT_LOG)
class FSE_DOCUMENT_LOG_Admin(admin.ModelAdmin):
    date_hierarchy = "date"
    list_display = ["id", "doc_type", "status_view"]

    @admin.display(description="Status", boolean=True)
    def status_view(self, obj):
        return True if obj.status == "DONE" else False
