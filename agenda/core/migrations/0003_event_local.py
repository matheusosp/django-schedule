# Generated by Django 3.1.1 on 2020-10-31 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201030_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='local',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
