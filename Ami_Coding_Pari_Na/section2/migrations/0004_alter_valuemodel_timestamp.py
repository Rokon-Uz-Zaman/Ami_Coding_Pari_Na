# Generated by Django 3.2.20 on 2023-08-16 07:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section2', '0003_alter_valuemodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valuemodel',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 16, 13, 32, 3, 13845), editable=False, null=True),
        ),
    ]