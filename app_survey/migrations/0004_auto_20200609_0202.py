# Generated by Django 3.0.4 on 2020-06-08 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_survey', '0003_auto_20200609_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='question',
            field=models.CharField(max_length=50),
        ),
    ]
