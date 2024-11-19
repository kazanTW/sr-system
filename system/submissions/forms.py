from django import forms
from .models import Submission


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = [
            'submitter_name', 'submitter_department', 'student_id',
            'phone_number', 'email', 'incident_date', 'case_category',
            'case_description', 'relief_sought'
        ]

    incident_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    evidence_file = forms.URLField(
        widget=forms.URLInput(attrs={
            'style': 'width: 100%; max-width: 600px;',
            'placeholder': '請輸入檔案或資料夾連結，建議使用 Google 雲端共享'}),
        required=False
    )
