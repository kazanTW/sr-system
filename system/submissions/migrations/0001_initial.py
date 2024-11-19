# Generated by Django 4.2.12 on 2024-10-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitter_name', models.CharField(max_length=100)),
                ('submitter_department', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=10)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('incident_date', models.DateField()),
                ('case_category', models.CharField(choices=[('校務建議', '校務建議'), ('校務申訴', '校務申訴'), ('會務建議', '會務建議'), ('會務申訴', '會務申訴'), ('校外申訴', '校外申訴')], max_length=50)),
                ('case_description', models.TextField()),
                ('relief_sought', models.TextField()),
                ('evidence_file', models.FileField(upload_to='evidence_files/')),
                ('submission_date', models.DateField()),
                ('status', models.CharField(choices=[('pending', '待受理'), ('accepted', '已受理'), ('processing', '處理中'), ('closing', '進入結案程序'), ('closed', '已簽署結案')], default='pending', max_length=20)),
            ],
        ),
    ]
