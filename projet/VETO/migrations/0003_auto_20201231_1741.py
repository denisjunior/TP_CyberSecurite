# Generated by Django 2.2.11 on 2020-12-31 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VETO', '0002_auto_20201231_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendezvous',
            name='heureDebut',
            field=models.TimeField(default=None),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='heureFin',
            field=models.TimeField(default=None),
        ),
    ]
