# Generated by Django 5.1.2 on 2024-11-19 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0004_evidencefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='evidence_file',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.DeleteModel(
            name='EvidenceFile',
        ),
    ]
