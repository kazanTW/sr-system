from django.contrib import admin
from django.utils.html import format_html
from .models import Submission


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('submitter_name',
                    'student_id',
                    'case_category',
                    'status',
                    'display_evidence_file',
                    'submission_date')
    list_filter = ('status', 'case_category')
    search_fields = ('submitter_name', 'student_id')
    ordering = ('-submission_date',)

    def display_evidence_file(self, obj):
        if obj.evidence_file:
            return format_html('<a href="{}" target="_blank">{}</a>',
                               obj.evidence_file, obj.evidence_file)
        return 'No Link'

    display_evidence_file.short_description = "佐證連結"
