# Generated by Django 3.1.1 on 2020-10-26 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20201026_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
