from django.db import models


class Submission(models.Model):
    STATUS_CHOICES = [
        ('pending', '待受理'),
        ('accepted', '已受理'),
        ('processing', '處理中'),
        ('closing', '進入結案程序'),
        ('closed', '已簽署結案'),
    ]

    submitter_name = models.CharField(max_length=100)
    submitter_department = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField()
    incident_date = models.DateField()
    case_category = models.CharField(
        max_length=50,
        choices=[
            ('校務建議', '校務建議'),
            ('校務申訴', '校務申訴'),
            ('會務建議', '會務建議'),
            ('會務申訴', '會務申訴'),
            ('校外申訴', '校外申訴'),
        ]
    )
    case_description = models.TextField()
    relief_sought = models.TextField()
    evidence_file = models.URLField(max_length=200, blank=True, null=True)
    submission_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return f'{self.submitter_name} - {self.student_id}'
