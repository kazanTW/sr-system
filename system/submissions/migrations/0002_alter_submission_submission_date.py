# Generated by Django 5.1.2 on 2024-11-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
